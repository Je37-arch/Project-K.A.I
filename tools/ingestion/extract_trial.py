"""Extract an explicitly bounded PDF range into ignored, unreviewed artifacts."""
import argparse
import hashlib
import json
from pathlib import Path
import pymupdf


def extract(source, first, last, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    private_root = Path(__file__).resolve().parents[2] / 'artifacts'
    if private_root not in output.parents:
        raise ValueError('Output must be a new directory beneath repository artifacts/.')
    with pymupdf.open(source) as doc:
        if doc.needs_pass:
            raise ValueError('Encrypted input requires an unlocked local copy.')
        if not 1 <= first <= last <= len(doc):
            raise ValueError('Page range must be inclusive, 1-based and within the PDF.')
        if output.exists():
            raise ValueError('Output already exists; choose a new trial directory.')
        output.mkdir(parents=True)
        rows = []
        for page_number in range(first, last + 1):
            page = doc[page_number - 1]
            raw = page.get_text(sort=True)
            text_name = f'page-{page_number:04}.txt'
            image_name = f'page-{page_number:04}.png'
            (output / text_name).write_text(raw, encoding='utf-8')
            page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(output / image_name)
            rows.append({
                'pdf_page': page_number, 'printed_page': None,
                'text_file': text_name, 'render_file': image_name,
                'characters': len(raw),
                'suspicious_control_characters': sum(ord(c) < 32 and c not in '\n\r\t' for c in raw),
                'embedded_image_count': len(page.get_images()),
                'review_status': 'unreviewed',
                'requires_visual_review': True,
            })
        manifest = {
            'schema_version': 1, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'source_page_count': len(doc), 'extractor': 'PyMuPDF',
            'extractor_version': pymupdf.VersionBind,
            'page_numbering': 'pdf_page is 1-based; printed_page requires manual mapping',
            'limitations': 'No OCR, math repair, diagram interpretation or automatic approval. Image counts omit vector diagrams. Text counts do not measure correctness.',
            'pages': rows,
        }
        (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
        return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--first', type=int, required=True)
    parser.add_argument('--last', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = extract(args.source, args.first, args.last, args.output)
    except (ValueError, OSError, RuntimeError) as error:
        parser.exit(1, f'Extraction failed: {error}\n')
    print(f"Extracted {len(manifest['pages'])} pages; all require review.")


if __name__ == '__main__':
    main()
