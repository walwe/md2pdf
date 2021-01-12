import click
from md2pdf.doc import Document
from md2pdf import __version__

CLI_NAME = "md2pdf"


@click.command()
@click.argument('md_file', type=click.Path(exists=True), required=True)
@click.option('--keep-html/--delete-html', default=False, help='Keep or delete intermediate html file')
@click.option('--output', '-o', type=click.Path(), help='Specify output file. Default: <md_file>.pdf')
@click.option('--css', '-c', type=click.Path(exists=True), help="Path to CSS file")
@click.option('--wkarg', '-w', multiple=True, type=str,
              help='Additional wkhtml2pdf arguments specified as --wkargs="--margin-top=0". '
                   'This option can be specified multiple times.')
@click.version_option(version=__version__, prog_name='md2pdf')
def cli(md_file, keep_html, output, css, wkarg):
    """md2pdf: A Markdown to PDF Converter"""
    doc = Document.from_markdown(md_file, stylesheet=css)
    if wkarg is not None:
        wkarg = dict(a.split('=') for a in wkarg)
    doc.save_to_pdf(keep_html=keep_html, pdf_file_name=output, extra_wkargs=wkarg)
