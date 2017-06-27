from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from unittest import TestCase

from md2pdf.doc import Document


class TestMd2Pdf(TestCase):

    def test_read_markdown_file(self):
        test_md = "# Test"
        with NamedTemporaryFile() as f:
            p = Path(f.name)
            p.write_text(test_md)
            doc = Document.from_markdown(str(p))
            self.assertEqual("<h1>Test</h1>\n", doc._body)

    def test_save_pdf(self):
        test_md = "# Test"
        with TemporaryDirectory() as d:
            pd = Path(d)
            test_md_file = pd / "test.md"
            test_md_file.write_text(test_md)
            doc = Document.from_markdown(test_md_file)
            doc.save_to_pdf()
            self.assertTrue(doc.pdf_file_name.exists())
