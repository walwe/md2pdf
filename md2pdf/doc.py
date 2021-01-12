import markdown2
import os.path
from subprocess import call
from pathlib import Path
from itertools import chain

#
# markdown2 extras:
# https://github.com/trentm/python-markdown2/wiki/Extras
#
DEFAULT_MARKDOWN_EXTRAS = [
    "tables",
    "footnotes",
    "fenced-code-blocks"
]


class Document(object):
    _DEFAULT_WK_KWARGS = {
        "--page-size": "A4",
        "--margin-top": "25mm",
        "--margin-bottom": "25mm",
        "--margin-left": "25mm",
        "--margin-right": "25mm",
    }
    _WK_CMD = "wkhtmltopdf"

    def __init__(self, body, file_name, stylesheet=None):
        self._body = body
        self._file_name = file_name
        self._html_file_name = None
        self._stylesheet = stylesheet

    @classmethod
    def from_markdown(cls, md_file, stylesheet=None, extras=DEFAULT_MARKDOWN_EXTRAS):
        md_file = Path(md_file)
        assert md_file.is_file()
        if stylesheet is not None:
            stylesheet = Path(stylesheet)
        with md_file.open() as f:
            return cls(
                markdown2.markdown(f.read(), extras=extras),
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

    def formatted_html(self):
        return self.template.format(
            **{
                'title': self._file_name.name,
                'body': self._body,
                'style': self.stylesheet
            })

    def save_to_html(self):
        with self.html_file_name.open(mode='w') as f:
            f.write(self.formatted_html())

    def save_to_pdf(self, pdf_file_name=None, keep_html=False, extra_wkargs=None):
        self.save_to_html()
        pdf_file_name = self.pdf_file_name if pdf_file_name is None else pdf_file_name

        wkargs = self._DEFAULT_WK_KWARGS.copy()
        wkargs['--title'] = self._file_name.name

        # merge user specified wk arguments
        if extra_wkargs is not None:
            wkargs.update(extra_wkargs)

        args = list(chain(*zip(wkargs.keys(), wkargs.values())))

        cmd = [self._WK_CMD] + args + [
           str(self.html_file_name),
           str(pdf_file_name)
        ]

        call(cmd)
        if not keep_html:
            self.html_file_name.unlink()
