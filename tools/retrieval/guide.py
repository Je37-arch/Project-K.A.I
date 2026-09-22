"""Conservative, template-routed diode guide prototype; no generated answers."""
import argparse
import json
from pathlib import Path
import re

from baseline import load_pack, require, validate, verify_sources

# Full-query matches only. These are intentionally narrow development templates,
# not a semantic classifier. Unrecognised requests never fall through to retrieval.
TOPICS = {
    'junction': ('junction',),
    'bias': ('bias',),
    'models': ('ideal', 'constant-drop'),
    'materials': ('materials',),
    'temperature': ('forward-temperature',),
    'reverse-temperature': ('reverse-temperature',),
    'resistance': ('resistance',),
    'piecewise': ('piecewise',),
    'thermal': ('thermal',),
    'exponential': ('exponential',),
}
PATTERNS = {
    'junction': [r'(?:what is|explain|describe) (?:a |the )?(?:pn|p n) junction(?: formation)?', r'how does (?:a |the )?depletion (?:region|layer) form'],
    'bias': [r'explain why forward bias changes the depletion region', r'(?:explain|compare|describe) (?:forward and reverse bias|diode bias|biasing)', r'what happens to the depletion (?:region|layer) (?:under|with|in) (?:forward|reverse) bias'],
    'models': [r'how would ideal and constant drop models treat the same conducting diode', r'(?:compare|explain) (?:the )?ideal and (?:constant drop|practical) (?:diode )?models', r'what is (?:the |an )?ideal diode(?: model)?'],
    'materials': [r'must every practical diode turn on at 0[ .]7 v', r'(?:compare|explain) (?:silicon and germanium|ge and si) (?:diodes|thresholds)', r'is 0[ .]7 v (?:a )?universal diode threshold'],
    'temperature': [r'at the same forward current what changes when a silicon diode becomes warmer', r'(?:what happens to|how does) (?:the )?forward voltage(?: change)? (?:when|as) (?:a )?silicon diode (?:warms|gets hotter) at (?:fixed|constant) current'],
    'reverse-temperature': [r'explain (?:the )?reverse current temperature approximation', r'how does silicon reverse current change with temperature'],
    'resistance': [r'why can dc resistance and small signal resistance differ at one operating point', r'(?:compare|explain|define) (?:dc|static) and (?:ac|dynamic|small signal) (?:diode )?resistance'],
    'piecewise': [r'does the voltage source drawn in a diode equivalent circuit supply power by itself', r'(?:explain|describe) (?:the |a )?piecewise linear (?:diode )?(?:model|equivalent circuit)', r'is (?:the )?diode equivalent circuit battery (?:real|a power supply)'],
    'thermal': [r'(?:what is|explain|define) (?:the )?thermal voltage', r'why (?:must|should) thermal voltage use kelvin'],
    'exponential': [r'(?:what is|explain|state) (?:the )?(?:shockley|exponential diode|diode current) equation'],
}


def normalise(query):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 .]', ' ', query.lower().replace('-', ' '))).strip(' .')


def decide(pack, query, include_drafts=False):
    validate(pack)
    require(isinstance(query, str) and len(query) <= 4000, 'Query must be text of at most 4000 characters.')
    result = dict(engine='diode-template-guide-v1', generated=False, pack_id=pack['pack_id'],
                  pack_version=pack['version'], course_id=pack['course_id'], unit_id=pack['unit_id'],
                  cards=[], drafts_enabled=include_drafts)

    def stop(status, reason, message):
        return dict(result, status=status, reason=reason, message=message)

    if pack['course_id'] != 'ECC-211' or pack['unit_id'] != 'diode-foundations':
        return stop('abstain', 'unsupported_pack_scope', 'This guide supports the ECC-211 diode-foundations unit only.')
    q = normalise(query)
    if not q:
        return stop('clarify', 'empty_question', 'Which diode concept would you like to study?')
    if re.search(r'\b(invent|fabricate|fake)\b.*\b(citation|citations|page|sources?|reference)\b', q):
        return stop('abstain', 'unsupported_evidence_request', 'I can only return citations recorded in the course pack.')
    if re.search(r'\b(transistors?|amplifiers?|bjt|mosfet|rectifiers?|clippers?|clampers?|fourier|modulation|zener)\b', q):
        return stop('abstain', 'outside_unit', 'This prototype covers diode foundations only. That request includes topics outside its current scope.')
    if re.search(r'\b(notes?|professor|teacher)\b', q) and re.search(r'\b(different|disagree|conflict|instead)\b', q):
        return stop('clarify', 'source_conflict', 'Please supply the relevant note and its diode model or conditions so the sources can be compared.')
    if re.search(r'\b(graph|diagram|attached|image|circuit drawing)\b', q):
        return stop('clarify', 'visual_input_unsupported', 'This text-only prototype cannot read a supplied graph or circuit diagram. Provide its labelled values and context; calculation support is still pending.')
    if re.search(r'\b(calculate|compute|solve|find the current|how much)\b', q):
        if not re.search(r'\d', q):
            return stop('clarify', 'numerical_context_missing', 'Please state the circuit, component values, temperature and diode model. This prototype does not yet calculate numerical answers.')
        return stop('abstain', 'calculator_unavailable', 'Numerical solving is not implemented, even when values are supplied. No current or voltage result has been calculated.')
    topics = [topic for topic, patterns in PATTERNS.items() if any(re.fullmatch(pattern, q) for pattern in patterns)]
    if len(topics) != 1:
        return stop('clarify', 'unrecognised_request', 'I cannot map the complete request to a supported explanation yet. Ask one question about junction formation, bias, diode models, material thresholds, resistance, thermal voltage or the diode equation. For temperature effects, state what is held fixed.')
    topic = topics[0]
    required = TOPICS[topic]
    by_id = {card['id']: card for card in pack['cards']}
    if any(cid not in by_id for cid in required):
        return stop('abstain', 'missing_evidence', 'The required explanation cards are missing from this pack version.')
    chosen = [by_id[cid] for cid in required]
    if any(card['review']['status'] != 'educator_reviewed' for card in chosen) and not include_drafts:
        return stop('abstain', 'review_pending', 'The explanation is still awaiting subject review. Draft preview must be explicitly enabled for development.')
    for card in chosen:
        result['cards'].append(dict(card_id=card['id'], title=card['title'], body=card['body'],
                                    conditions=card['conditions'], review=card['review'],
                                    references=[dict(ref, credit=pack['sources'][ref['resource_id']]['credit']) for ref in card['references']]))
    draft = any(card['review']['status'] == 'draft' for card in chosen)
    return dict(result, status='draft_preview' if draft else 'reviewed_cards', topic=topic,
                reason='explicit_template_match', message='Unchanged explanation cards for a recognised template. Conditions and citations apply; this is not a generated or general-purpose answer.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pack', type=Path, required=True)
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
        output = decide(pack, args.query, args.include_drafts)
        output.update(pack_sha256=digest, source_files_verified=True)
        print(json.dumps(output, indent=2, ensure_ascii=True))
    except (ValueError, OSError, TypeError) as error:
        parser.exit(1, f'Cannot guide: {error}\n')


if __name__ == '__main__':
    main()
