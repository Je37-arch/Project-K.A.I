"""Local evidence-card retrieval experiment. No generated answers or network calls."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re

STOP = set('a an the is are was were be to of in on at for and or with what how why does do when it its this that my me explain would can'.split())


def tokens(text):
    return set(re.findall(r'[a-z0-9]+', text.lower())) - STOP


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def positive_int(value):
    return type(value) is int and value > 0


def validate(pack):
    require(isinstance(pack, dict) and pack.get('schema_version') == 1, 'Unsupported pack schema.')
    for key in ('pack_id', 'version', 'course_id', 'unit_id'):
        require(text(pack.get(key)), f'Missing {key}.')
    sources = pack.get('sources')
    require(isinstance(sources, dict) and sources, 'Sources must be a nonempty object.')
    for rid, src in sources.items():
        require(text(rid) and isinstance(src, dict), 'Invalid source record.')
        require(text(src.get('credit')), 'Source credit required.')
        require(isinstance(src.get('sha256'), str) and re.fullmatch('[0-9a-f]{64}', src['sha256']), 'Invalid source hash.')
        require(positive_int(src.get('page_count')), 'Invalid source page count.')
    require(isinstance(pack.get('cards'), list), 'Cards must be a list.')
    ids = set()
    for card in pack['cards']:
        require(isinstance(card, dict), 'Card must be an object.')
        for key in ('id', 'title', 'body'):
            require(text(card.get(key)), f'Card missing {key}.')
        require(card['id'] not in ids, 'Duplicate card ID.')
        ids.add(card['id'])
        for key in ('tags', 'conditions'):
            require(isinstance(card.get(key), list) and all(text(v) for v in card[key]), f'Invalid {key}.')
        review = card.get('review')
        require(isinstance(review, dict) and review.get('status') in ('draft', 'educator_reviewed'), 'Invalid review status.')
        require(text(review.get('checked_by')) and text(review.get('method')), 'Review provenance required.')
        if review['status'] == 'educator_reviewed':
            require(text(review.get('reviewer')) and text(review.get('reviewed_at')), 'Educator review requires reviewer and date.')
        refs = card.get('references')
        require(isinstance(refs, list) and refs, 'Card needs source references.')
        for ref in refs:
            require(isinstance(ref, dict) and ref.get('resource_id') in sources, 'Unknown citation source.')
            src = sources[ref['resource_id']]
            require(ref.get('source_sha256') == src['sha256'], 'Citation source version mismatch.')
            require(positive_int(ref.get('pdf_page')) and ref['pdf_page'] <= src['page_count'], 'Citation page outside source.')
            require(text(ref.get('printed_page')) and text(ref.get('section')), 'Printed page and section required.')
    return pack


def load_pack(path):
    raw = Path(path).read_bytes()
    return validate(json.loads(raw)), hashlib.sha256(raw).hexdigest()


def verify_sources(pack, paths):
    require(set(paths) == set(pack['sources']), 'Supply exactly one local file per source ID.')
    for rid, path in paths.items():
        digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
        require(digest == pack['sources'][rid]['sha256'], f'Local source hash mismatch: {rid}.')


def retrieve(pack, query, include_drafts=False, limit=3):
    validate(pack)
    require(isinstance(query, str) and len(query) <= 4000, 'Query must be text of at most 4000 characters.')
    require(type(limit) is int and 1 <= limit <= 5, 'Limit must be 1–5.')
    eligible = [c for c in pack['cards'] if include_drafts or c['review']['status'] == 'educator_reviewed']
    base = {'engine': 'lexical-card-baseline-v1', 'generated': False,
            'pack_id': pack['pack_id'], 'pack_version': pack['version'],
            'course_id': pack['course_id'], 'unit_id': pack['unit_id'],
            'drafts_enabled': include_drafts, 'matches': [],
            'warning': 'Related evidence only; keyword overlap does not establish that a card answers the question.'}
    q = tokens(query)
    if not q:
        return dict(base, status='clarification_needed', message='Enter a question with a topic or concept.')
    if not eligible:
        return dict(base, status='no_eligible_cards', message='No reviewed cards available. Draft preview requires explicit opt-in.')
    docs = [tokens(c['title'] + ' ' + ' '.join(c['tags']) + ' ' + c['body']) for c in eligible]
    # Fixed experimental rule: at least two distinct query terms must overlap.
    # No confidence probability or semantic sufficiency claim is attached to this score.
    scores = []
    for c, d in zip(eligible, docs):
        overlap = q & d
        if len(overlap) < 2:
            continue
        score = sum(math.log(1 + len(docs) / (1 + sum(t in other for other in docs))) for t in overlap) / math.sqrt(len(d))
        scores.append((score, c, overlap))
    for score, c, overlap in sorted(scores, key=lambda item: (-item[0], item[1]['id']))[:limit]:
        refs = [dict(ref, credit=pack['sources'][ref['resource_id']]['credit']) for ref in c['references']]
        base['matches'].append({'card_id': c['id'], 'title': c['title'], 'body': c['body'],
                                'conditions': c['conditions'], 'review': c['review'],
                                'references': refs, 'score': round(score, 6),
                                'matched_terms': sorted(overlap)})
    return dict(base, status='evidence_candidates' if base['matches'] else 'no_supported_match',
                message='Inspect related cards and their conditions.' if base['matches'] else 'No supported match under this lexical rule; rephrase or supply more context.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pack', required=True, type=Path)
    parser.add_argument('--query', required=True)
    parser.add_argument('--source', action='append', default=[], metavar='ID=PATH')
    parser.add_argument('--include-drafts', action='store_true')
    args = parser.parse_args()
    try:
        pack, digest = load_pack(args.pack)
        paths = {}
        for item in args.source:
            rid, sep, path = item.partition('=')
            require(sep and rid not in paths and path, 'Use one --source ID=PATH per resource.')
            paths[rid] = path
        verify_sources(pack, paths)
        result = retrieve(pack, args.query, args.include_drafts)
        result.update(pack_sha256=digest, source_files_verified=True)
        print(json.dumps(result, indent=2, ensure_ascii=True))
    except (ValueError, OSError, TypeError) as error:
        parser.exit(1, f'Cannot retrieve: {error}\n')


if __name__ == '__main__':
    main()
