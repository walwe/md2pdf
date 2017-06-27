import markdown2
import os.path
from subprocess import call
from pathlib import Path


class Document(object):

    def __init__(self, body, file_name, stylesheet=None):
        self._body = body
        self._file_name = file_name
        self._html_file_name = None
        self._stylesheet = stylesheet

    @staticmethod
    def from_markdown(md_file, stylesheet=None):
        md_file = Path(md_file)
        assert md_file.is_file()
        if stylesheet is not None:
            stylesheet = Path(stylesheet)
        with md_file.open() as f:
            return Document(
                markdown2.markdown(f.read(), extras=["tables"]),
                md_file,
                stylesheet
            )

    @property
    def template(self):
        fn = Path(os.path.dirname(__file__)) / 'res/template.html'
        return fn.open().read()

    @property
    def stylesheet(self):
        if self._stylesheet is not None:
            fn = self._stylesheet
        else:
            fn = Path(os.path.dirname(__file__)) / 'res/css/github.css'
        assert fn.is_file()
        return fn.open().read()

    @property
    def html_file_name(self):
        return self._file_name.with_suffix('.temp.html')

    @property
    def pdf_file_name(self):
        return self._file_name.with_suffix('.pdf')

    def save_to_html(self):
        self.html_file_name.write_text(self.template.format(
            **{
                'title': self._file_name.name,
                'body': self._body,
                'style': self.stylesheet
            }
        ))

    def save_to_pdf(self, pdf_file_name=None, keep_html=False):
        self.save_to_html()
        pdf_file_name = self.pdf_file_name if pdf_file_name is None else pdf_file_name
        call(["wkhtmltopdf",
              "-q",
              "--title", self._file_name.name,
              self.html_file_name,
              pdf_file_name])
        if not keep_html:
            self.html_file_name.unlink()
