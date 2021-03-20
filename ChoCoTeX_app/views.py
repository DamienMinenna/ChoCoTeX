from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import os
from os import listdir
from os.path import isfile, join
import subprocess
from subprocess import STDOUT, check_output
import time
import sys

from random import randint
import re

from django.conf import settings

from .writeTeX import writeuser_tex, writeuser_cmd

isServer = False
allowedPDF = 10000


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def home(request):

    fontsize = 34
    display_error = 0
    display_pdf = False
    color = '#000000'

    if isServer:
        user_id = randint(10000001, 99999999)
    else:
        user_id = 10000000

    return render(request, 'home.html', {
        'display_error': display_error,
        'display_pdf': display_pdf,
        'fontsize' : fontsize,
        'color' : color,
        'user_id' : user_id,
        })


def generate_PDF(request):

    security_issues = False

    my_tex_form_element = ['user_id','fulltextarea','font_size','favcolor','env_tex']

    for i in my_tex_form_element:
        if i not in request.GET :
            security_issues = True
            print(security_issues)

    if not security_issues:
        user_id = request.GET['user_id']
        text_tex = request.GET['fulltextarea']
        fontsize = request.GET['font_size']
        color = request.GET['favcolor']
        env_tex = request.GET['env_tex']
        display_error = 0

        # Check and security
        if not user_id.isnumeric():
            if isServer:
                user_id = randint(10000001, 99999999)
            else:
                user_id = 10000000

        elif ((int(user_id) < 10000000) or (int(user_id) > 99999999)):
            if isServer:
                user_id = randint(10000001, 99999999)
            else:
                user_id = 10000000

        # Check and security
        if not isFloat(fontsize):
            fontsize = 34
            display_error = 3
            display_pdf = False
            loc_pdf_File = ' '
            security_issues = True

        elif ((float(fontsize) < 1.) or (float(fontsize) > 100.)):
            fontsize = 34
            display_error = 3
            display_pdf = False
            loc_pdf_File = ' '
            security_issues = True

        # Check and security
        if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
            display_error = 4
            color = '#000000'
            display_pdf = False
            loc_pdf_File = ' '
            security_issues = True

        # Check and security
        if ((int(env_tex) < 1) or (int(env_tex) > 4)):
            display_error = 5
            display_pdf = False
            loc_pdf_File = ' '
            security_issues = True

    else:
        if isServer:
            user_id = randint(10000001, 99999999)
        else:
            user_id = 10000000
        text_tex = ''
        fontsize = 34
        color = '#000000'
        display_error = 6
        display_pdf = False
        loc_pdf_File = ' '



    if not security_issues:
        if not text_tex:
            text_tex = ''
            display_pdf = False
            loc_pdf_File = ' '

        else:
            display_pdf = True
            writeuser_tex(text_tex,int(env_tex))
            writeuser_cmd(fontsize,color)

            # Check if the number of PDF file remains small
            if len([f for f in listdir('media/pdf/') if isfile(join('media/pdf/', f))]) < allowedPDF:

                srtcmd = (r'pdflatex -output-directory=media/pdf/ latex/ChoCoTeX_temp.tex')
                # os.system(srtcmd)
                proc = subprocess.Popen(srtcmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)

                try:
                    outs, errs = proc.communicate(timeout=15)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    outs, errs = proc.communicate()
                    display_error = 1
                    display_pdf = False
                    loc_pdf_File = ' '

                if os.path.exists('media/pdf/ChoCoTeX_temp.pdf'):
                    os.system('mv media/pdf/ChoCoTeX_temp.pdf media/pdf/ChoCoTeXv'+ str(user_id) + '.pdf')
                    loc_pdf_File = ('/media/pdf/ChoCoTeXv'+ str(user_id) + '.pdf')
                else:
                    display_error = 1
                    display_pdf = False
                    loc_pdf_File = ' '

            else:
                display_error = 2
                display_pdf = False
                loc_pdf_File = ' '

    #security_issues

    print('file:',loc_pdf_File)
    return render(request, 'home.html', {
        'text_tex': text_tex,
        'display_error': display_error,
        'display_pdf': display_pdf,
        'fontsize' : fontsize,
        'color' : color,
        'user_id' : user_id,
        'loc_pdf_File': loc_pdf_File
        })
