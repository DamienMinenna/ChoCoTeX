# GroTeX

GroTeX is an open-source web application to generate vector PDF with a transparent background from LaTeX equations. Those PDF can be copied in the clipboard and immediately pasted in typesetting or presentation softwares, such as Word or PowerPoint. GroTeX use the web framework Django.

## Installation

Commands must be executed on a shell terminal.
GroTeX needs pdflatex to work. Check on a terminal it is installed.

```bash
pdflatex --version
```

You also need the last version of Python (check the version with "python3 -V").

```bash
sudo apt-get install python3.7
```

Install Django.

```bash
python -m pip install Django
```

You can download the git project or directly clone it.

```bash
git clone https://github.com/DamienMinenna/GroTeX.git
```

Finally just launch the server.

```bash
python manage.py migrate
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

You can modify the font size and the color. The background is transparent.
After the creation of the PDF, you can use the "Copy PDF to clipboard" and the download functions.

### Server usage

To manage several users (or several opened windows), just modify the value "isServer" to "True" in the GroTeX_app/views.py. Generated PDF will get random id.
Then run on another terminal tab
```bash
python manage.py pdf_management
```
This will remove generated PDF after 10 minutes (check every 5 minutes).

## Contributing

Pull requests on the git project are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
