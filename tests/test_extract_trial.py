import importlib.util
import tempfile
import unittest
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('extract_trial', ROOT / 'tools/ingestion/extract_trial.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ExtractionTests(unittest.TestCase):
    def test_anchors_and_preservation(self):
        (ROOT / 'artifacts').mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / 'artifacts') as folder:
            folder = Path(folder)
            source = folder / 'synthetic.pdf'
            with pymupdf.open() as doc:
                for label in ['FIRST PAGE', 'SECOND PAGE']:
                    doc.new_page().insert_text((72, 72), label)
                doc.save(source)
            output = folder / 'result'
            result = module.extract(source, 2, 2, output)
            self.assertEqual(result['pages'][0]['pdf_page'], 2)
            self.assertEqual(result['pages'][0]['review_status'], 'unreviewed')
            self.assertIn('SECOND PAGE', (output / 'page-0002.txt').read_text())
            self.assertNotIn('FIRST PAGE', (output / 'page-0002.txt').read_text())
            self.assertTrue((output / 'page-0002.png').exists())
            with self.assertRaises(ValueError):
                module.extract(source, 2, 2, output)
            for first, last in [(0, 1), (2, 1), (1, 3)]:
                with self.assertRaises(ValueError):
                    module.extract(source, first, last, folder / 'invalid')
            self.assertFalse((folder / 'invalid').exists())
            with self.assertRaises(ValueError):
                module.extract(source, 1, 1, ROOT / 'public-extraction')


if __name__ == '__main__':
    unittest.main()
