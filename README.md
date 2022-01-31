# md2pdf: A Python Markdown to PDF Converter

Convert Markdown to PDF using markdown2 and wkhtmltopdf.

## Install

Install the wkhtmltopdf package first, on Debian/Ubuntu:

```
sudo apt install wkhtmltopdf
```

And then install md2pdf to your Python environment:
```
pip install .
```
or:
```
python setup.py install
```

## Usage
```
python -m md2pdf <markdown-file.md>
```

```
python -m md2pdf <markdown-file.md> -o <pdf-file.pdf>
```

Please run `python -m md2pdf --help` to find more usage.
