import click
from md2pdf.doc import Document
from md2pdf import version


@click.command()
@click.argument('md_file', type=click.Path(exists=True), required=True)
@click.option('--keep-html/--delete-html', default=False, help='Keep or delete intermediate html file')
@click.option('--output', '-o', type=click.Path(), help='Specify output file. Default: <md_file>.pdf')
@click.option('--css', '-c', type=click.Path(exists=True), help="Path to CSS file")
@click.version_option(version=version, prog_name='md2pdf')
def cli(md_file, keep_html, output, css):
    """md2pdf: A Markdown to PDF Converter"""
    doc = Document.from_markdown(md_file, stylesheet=css)
    doc.save_to_pdf(keep_html=keep_html, pdf_file_name=output)


if __name__ == "__main__":
    cli()

