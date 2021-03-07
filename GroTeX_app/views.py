import os
import subprocess
from subprocess import STDOUT, check_output
import time
import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render

def writeuser_tex(text_tex,env):

    if env == 1:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"\begin{align*}")
        text_file.write("\n")
        text_file.write(r"%s" % text_tex)
        text_file.write("\n")
        text_file.write(r"\end{align*}")
        text_file.close()
    elif env == 2:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"\begin{equation*}")
        text_file.write("\n")
        text_file.write(r"%s" % text_tex)
        text_file.write("\n")
        text_file.write(r"\end{equation*}")
        text_file.close()
    elif env == 3:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"$ %s $" % text_tex)
        text_file.close()
    elif env == 4:
        text_file = open("latex/user_eq.tex", "w")
        text_file.write(r"%s" % text_tex)
        text_file.close()


def home(request):

    fontsize = 34
    display_error_compitex = 'display:none;'
    display_pdf = 'display:none;'
    color = '#000000'

    return render(request, 'home.html', {
        'display_error_compitex': display_error_compitex,
        'display_pdf': display_pdf,
        'fontsize' : fontsize,
        'color' : color,
        })


def generate_PDF(request):

    text_tex = request.GET['fulltextarea']
    fontsize = request.GET['font_size']
    color = request.GET['favcolor']
    env_tex = request.GET['env_tex']
    display_error_compitex = 'display:none;'

    if not text_tex:
        text_tex = ''
        display_pdf = 'display:none;'

    else:
        display_pdf = ' '

        writeuser_tex(text_tex,int(env_tex))

        text_file = open(r"latex/user_cmd.tex", "w")
        text_file.write(r"\def\myfontsize{%s}" % str(fontsize))
        text_file.write("\n")
        text_file.write(r"\def\myfontsizeplus{%s}" % str(float(fontsize)+5))
        text_file.write("\n")
        text_file.write(r"\definecolor{mycolor}{HTML}{%s}" % color[1:])
        text_file.close()

        srtcmd = (r'pdflatex -output-directory=static/img/ latex/GroTeX.tex')

        # os.system(srtcmd)
        proc = subprocess.Popen(srtcmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)

        try:
            outs, errs = proc.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            display_error_compitex = ' '
            display_pdf = 'display:none;'

    return render(request, 'home.html', {
        'text_tex': text_tex,
        'display_error_compitex': display_error_compitex,
        'display_pdf': display_pdf,
        'fontsize' : fontsize,
        'color' : color,
        })
