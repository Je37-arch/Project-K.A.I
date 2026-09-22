"""Run non-generative development cases; never score or run held-out questions."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'retrieval'))
from baseline import load_pack, require, retrieve, verify_sources
from guide import decide


def load_cases(path):
    raw = Path(path).read_bytes()
    cases = [json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
    ids = set()
    for case in cases:
        require(isinstance(case, dict), 'Each case must be an object.')
        require(case.get('split') == 'development', 'Development runner rejects held-out or missing split labels.')
        for key in ('id','family','category','prompt','expected_behavior_draft','review_status'):
            require(isinstance(case.get(key), str) and case[key].strip(), f'Missing case field: {key}')
        require(case['id'] not in ids, 'Duplicate case ID.')
        require(len(case['prompt']) <= 4000, 'Prompt exceeds query budget.')
        ids.add(case['id'])
    require(bool(cases), 'Empty dataset.')
    return cases, hashlib.sha256(raw).hexdigest()


def run(pack, cases, include_drafts=False):
    rows=[]
    for case in cases:
        # Only the prompt reaches either answering component, never the expected behaviour.
        start=time.perf_counter()
        lexical=retrieve(pack,case['prompt'],include_drafts)
        guide=decide(pack,case['prompt'],include_drafts)
        rows.append(dict(id=case['id'],family=case['family'],category=case['category'],
                         lexical=lexical,guide=guide,
                         pair_elapsed_seconds=time.perf_counter()-start,
                         correctness_score=None,review_required=True))
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pack',type=Path,required=True)
    parser.add_argument('--cases',type=Path,required=True)
    parser.add_argument('--source',action='append',default=[])
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--include-drafts',action='store_true')
    args=parser.parse_args()
    try:
        output=args.output.resolve()
        root=Path(__file__).resolve().parents[2]/'evals/results'
        require(root in output.parents,'Output must be beneath ignored evals/results/.')
        require(not output.exists(),'Do not overwrite previous results; choose a new output.')
        cases,case_hash=load_cases(args.cases)
        pack,pack_hash=load_pack(args.pack)
        paths={}
        for item in args.source:
            rid,sep,path=item.partition('=')
            require(sep and path and rid not in paths,'Use one --source ID=PATH per resource.')
            paths[rid]=path
        verify_sources(pack,paths)
        report=dict(schema_version=1,dataset_sha256=case_hash,pack_sha256=pack_hash,
                    model=None,source_files_verified=True,scope='development-only; no automatic quality scores',
                    results=run(pack,cases,args.include_drafts))
        output.parent.mkdir(parents=True,exist_ok=True)
        with output.open('x',encoding='utf-8') as f: json.dump(report,f,indent=2)
        print(f'Recorded {len(cases)} cases. Subject scoring remains pending.')
    except (ValueError,OSError,TypeError) as error:
        parser.exit(1,f'Cannot evaluate: {error}\n')


if __name__=='__main__': main()
