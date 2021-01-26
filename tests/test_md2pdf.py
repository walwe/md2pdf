from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from unittest import TestCase
from PIL import Image
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

    def test_local_image(self):
        image_name = "TestImage.jpg"
        test_md = f"# Test\n![Test]({image_name})"
        image = Image.new('RGB', size=(1, 1))

        with TemporaryDirectory() as d:
            pd = Path(d)
            image.save(str(pd / image_name))
            test_md_file = pd / "test.md"
            test_md_file.write_text(test_md)
            doc = Document.from_markdown(test_md_file)
            doc.save_to_pdf()
            self.assertTrue(doc.pdf_file_name.exists())

    def test_local_image_in_subdir(self):
        image_name = "TestImage.jpg"
        sub_dir = "´testsubdir"
        test_md = f"# Test\n![Test]({sub_dir}/{image_name})"
        image = Image.new('RGB', size=(1, 1))

        with TemporaryDirectory() as d:
            pd = Path(d)
            (pd / sub_dir).mkdir()
            image.save(str(pd / sub_dir / image_name))
            test_md_file = pd / "test.md"
            test_md_file.write_text(test_md)
            doc = Document.from_markdown(test_md_file)
            doc.save_to_pdf()
            self.assertTrue(doc.pdf_file_name.exists())

    def test_local_image_outside_md_path(self):
        with TemporaryDirectory() as d:
            with TemporaryDirectory() as im_d:
                image_name = "TestImage.jpg"
                test_md = f"# Test\n![Test]({im_d}/{image_name})"
                image = Image.new('RGB', size=(1, 1))
                pd = Path(d)
                image.save(str(Path(im_d) / image_name))
                test_md_file = pd / "test.md"
                test_md_file.write_text(test_md)
                doc = Document.from_markdown(test_md_file)
                doc.save_to_pdf()
                self.assertTrue(doc.pdf_file_name.exists())
                # TODO: how to fix?
                self.assertTrue(False)
