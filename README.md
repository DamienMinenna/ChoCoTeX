# GroTeX

GroTeX is an open-source web application to generate vector PDF with a transparent background from LaTeX equations. Those PDF can be copied in the clipboard and immediately pasted in typesetting or presentation softwares, such as Word or PowerPoint. GroTeX use the web framework Django.

## Installation

GroTeX needs pdflatex to work. Check on a terminal it is installed.

```bash
pdflatex --version
```

You also need the last version of Python (check the version with "python3 -V").

```bash
sudo apt-get install python3.7
```

Finally install Django.

```bash
python -m pip install Django
```

You can download the git project or directly clone it.

```bash
git clone ...
```

Finally just launch the server. (Migration are not required).

```bash
python manage.py runserver
```

The following message should appear

```bash
Django version 3.1.7, using settings 'GroTeX.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

You must leave open the terminal.

Now, you can open GroTeX using any web browser at the address: http://127.0.0.1:8000/

## Usage

Write your LaTeX equation in the text area. You do not need to add $$. For example:
```
{\bf g}_{\rm cano} = \frac{n_\phi n_{\rm g}}{c^2} {\bf E} \times {\bf H}
```

You can modify the font size and the color. The background is transparent. You can use the "Copy PDF to clipboard" button.

### Warning

If you use non valide TeX commands or the incorrect environment, such as a math command in the text environment, pdflatex will crash. A 15 seconds timer is set before the pdflatex process is killed.

## Contributing

Pull requests on the git project are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
