import click
from md2pdf.doc import Document


@click.command()
@click.argument('md_file', type=click.Path(exists=True), required=True)
@click.option('--keep-html/--delete-html', default=False, help='Keep or delete intermediate html file')
@click.option('--output', '-o', type=click.Path())
def main(md_file, keep_html, output):
    doc = Document.from_markdown(md_file)
    doc.save_to_pdf(keep_html=keep_html, pdf_file_name=output)


if __name__ == "__main__":
    main()

