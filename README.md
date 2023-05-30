# md2pdf: A Python Markdown to PDF Converter

Convert Markdown to PDF using [markdown2](https://github.com/trentm/python-markdown2) and [wkhtmltopdf](https://wkhtmltopdf.org/).

## Install

### Archlinux
Use the provided [AUR package](https://aur.archlinux.org/packages/md2pdf-git/)

### Other Linux Systems

Install the wkhtmltopdf package first

* Debian/Ubuntu
  ```
  sudo apt install wkhtmltopdf
  ```
* Others
  ```
  sudo pip install wkhtmltopdf
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
You can run md2pdf using
* the entry-script `md2pdf`
* calling the module `python -m md2pdf`

```
md2pdf <markdown-file.md>
```

```
md2pdf <markdown-file.md> -o <pdf-file.pdf>
```

Please run `md2pdf --help` to find more usage.
```
Options:
  --keep-html / --delete-html  Keep or delete intermediate html file
  -o, --output PATH            Specify output file. Default: <md_file>.pdf
  -c, --css PATH               Path to CSS file
  -w, --wkarg TEXT             Additional wkhtml2pdf arguments specified as
                               --wkargs="--margin-top=0". This option can be
                               specified multiple times.
  --version                    Show the version and exit.
  --help                       Show this message and exit.
```

## License
MIT licensed as found in the [LICENSE](LICENSE) file.
