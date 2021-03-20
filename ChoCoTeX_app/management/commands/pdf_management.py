from django.core.management.base import BaseCommand, CommandError

import threading
import os
import os.path, time
from os import listdir
from os.path import isfile, join

def rm_PDFfile():
    threading.Timer(5*60, rm_PDFfile).start()

    # Remove aux and log files
    auxfile = 'media/pdf/GroTeX_temp.aux'
    if os.path.exists(auxfile):
        os.system('rm ' + auxfile)

    logfile = 'media/pdf/GroTeX_temp.log'
    if os.path.exists(logfile):
        os.system('rm ' + logfile)

    # Get the list of pdf item
    onlyfiles = [f for f in listdir('media/pdf/') if isfile(join('media/pdf/', f))]

    for f in onlyfiles:
        pdffile = 'media/pdf/' + f

        t = time.time()

        # Remove PDF files after time expired
        if t - os.path.getctime(pdffile) > 10*60:
            os.system('rm ' + pdffile)

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Starting pdf_management.py')

        rm_PDFfile()
