import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('run_development',ROOT/'tools/evaluation/run_development.py')
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)

class DevelopmentRunnerTests(unittest.TestCase):
    def setUp(self):
        self.case=dict(id='D1',split='development',family='test-family',category='explanation',prompt='amber switch',expected_behavior_draft='SECRET_EXPECTED_KEY',review_status='pending')

    def load(self,rows):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'cases.jsonl';p.write_text(''.join(json.dumps(r)+'\n' for r in rows))
            return e.load_cases(p)

    def test_rejects_heldout_and_duplicates(self):
        held=copy.deepcopy(self.case);held['split']='held-out'
        for rows in [[held],[self.case,self.case],[]]:
            with self.assertRaises(ValueError): self.load(rows)

    def test_requires_expected_behavior_but_never_sends_it(self):
        with patch.object(e,'retrieve',return_value={}) as retrieve, patch.object(e,'decide',return_value={}) as decide:
            rows=e.run({},[self.case],True)
            self.assertEqual(retrieve.call_args.args,({},'amber switch',True))
            self.assertEqual(decide.call_args.args,({},'amber switch',True))
            self.assertNotIn('SECRET_EXPECTED_KEY',json.dumps(rows))
            self.assertIsNone(rows[0]['correctness_score'])

    def test_checksum_changes_with_dataset(self):
        _,first=self.load([self.case]);changed=copy.deepcopy(self.case);changed['prompt']='violet dial'
        _,second=self.load([changed]);self.assertNotEqual(first,second)

    def test_malformed_case(self):
        for mutation in [dict(prompt='x'*4001),dict(family=''),dict(split=None)]:
            c=dict(self.case,**mutation)
            with self.assertRaises(ValueError):self.load([c])

if __name__=='__main__':unittest.main()
