#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import subprocess
import tarfile
import urllib
import zipfile
import clint
from clint.textui import progress
import requests
from pathlib import Path

os_name = os.name
jetzt_datei_namen = ''
source_path = ''
herunterladen_datei_namen = ''

def loeschen_herunterladen_datei():
    print 'hello'
    #  müsst hinzufügen die herunterladen_datei_namen für diesem dingen

def anrufen_skipt(skript_pfad):
    subprocess.call('./kompilieren_skript/' + skript_pfad)
def finden_code_pfad(skript_pfad):
    subprocess.call("./" + skript_pfad)


def find_source_path():
    dir_contents = os.listdir(os.getcwd())
    for x in dir_contents:
        if (jetzt_datei_namen[:4] in x) and (os.path.isdir(x)) and (x != 'kompilieren_skript'):
            source_path = os.getcwd() + '/' + x
            return
    print ('Kann nicht gefunden die Extrahiert datei, tut mir leid')
    return



def shaffen_datei_namen(url):  # Bekomment die namen aus die datei fuer entpack
    for i in range(len(url) - 1, -1, -1):
        if url[i] == '/':
            return url[i + 1:]


def finden_art_und_entpack():
    file_extension = ''
    for i in range(0, len(jetzt_datei_namen)):
        if jetzt_datei_namen[i] == '.':
            if ((jetzt_datei_namen[i + 1]).isdigit() and (jetzt_datei_namen[i - 1]).isdigit()) != True:
                file_extension = jetzt_datei_namen[i:]
                break
    if file_extension == '':
        print('Datei ist korrupt, tut mir leid')
    if file_extension == ".zip" or file_extension == '.gzip':
        # File is a zip
        fileHandle = open('packageFile', 'rb')
        zipfile.ZipFile("packageName").extractall()

    elif file_extension == '.tar' or file_extension == '.tar.gz' or file_extension == '.tgz':
        #  File is either a tar or tar.gz and can be extracted with 'tar'
        tar = tarfile.open(jetzt_datei_namen)
        tar.extractall()
        tar.close()
        kopilieren_code_fall_benoetigt()
    # elif file_extension == '.tgz':
    #     tar = tarfile.open(current_file_name)
    #     for x in tar:
    #         tar.extract(x, os.getcwd() + "/" + "PythonSource")
    #         if x.name.find('.tgz') != -1 or x.name.find('.tar') != -1:

    else:
        print("Datei erweiterung nicht gefunden!")


def entpack_datei(archive_type):  # NOTE: 0 = zip / 1 = tar
    if archive_type is 0:
        zipfile.ZipFile("packageFile").extractall()
    elif archive_type is 1:
        tarfile.TarFile('packageFile').extractall()
    else:
        print("type pass failed")


def konfigurieren_code(source_type, compile_arguments):
    if source_type is 0 or source_type is 10 and "posix" in os:  # os.name returns 'posix' on OSX systems
        subprocess_arguments = ('sudo', './configure')
        process = subprocess.Popen(subprocess_arguments, stdout=subprocess.PIPE)
        print("Configuring...")
        output = process.stdout.read()
        print(output)
    else:
        print('source type not recognized')


def kopilieren_code_fall_benoetigt():  # compileCommands can be left null if not necessary
    if ('Python' in jetzt_datei_namen) and ('3' not in jetzt_datei_namen):  #  Python 2
        print('Nicht Umgesetzt wurden noch')
    elif ('Python' in jetzt_datei_namen) and ('3' in jetzt_datei_namen):  #  Python 3
        anrufen_skipt('compile_python3.sh')  # Ich kennt dies können besser gemacht
    elif 'gcc' in jetzt_datei_namen:
        anrufen_skipt('compile_gcc.sh')

def herunterladen_mit_ftp(url):
    global jetzt_datei_namen  # bekommen var Berichtigungen
    jetzt_datei_namen = shaffen_datei_namen(url)
    source_exists = os.path.exists(os.path.abspath(jetzt_datei_namen))
    if not source_exists:
        urllib.urlretrieve(url, jetzt_datei_namen)  # TODO zulassen datei zu speeren ändern Ort sein
    finden_art_und_entpack()
    kopilieren_code_fall_benoetigt()
    # NOTE: url müsst mit ftp:// beginnern

    # TODO: macht das datei nicht herunterladen ob datei Existiert


def herunterladen_mit_http(package_name, url):
    global jetzt_datei_namen  # bekommen var Berichtigungen
    jetzt_datei_namen = shaffen_datei_namen(url) #  Dies müsst in alles herunterladen methoden sein!
    file_name = shaffen_datei_namen(url)
    print 'herunterladen gestartet'
    responce = requests.get(url, stream=True)
    if not os.path.exists(os.path.abspath(jetzt_datei_namen)):
        with open(file_name, 'wb') as f:
            for block in responce.iter_content(chunk_size=1024):
                if block:
                    f.write(block)
    print 'herunterladen fertig'
    finden_art_und_entpack()
    kopilieren_code_fall_benoetigt()




    # NOTE: url must be prefixed with http:// or https://


def klon_mit_git(package_name, url):
    urllib.urlretrieve(url, 'packageFile')
    # NOTE url must be prefixed with git://


def klon_mit_subversion(package_name, url):
    urllib.urlretrieve(url, 'packageFile')
    # NOTE url must be prefixed with subverion prefix


def herunterladen_package(type, package_name):
    index = 0
    lines = [line.rstrip('\n') for line in open("packages")]
    for i in range(0, len(lines)):
        if lines[i] == package_name:
            index = i
            break
    url_lines = [line.rstrip('\n') for line in open("packageURL")]
    url = url_lines[index]
    if type == 0:
        herunterladen_mit_ftp(url)
    elif type is 1:
        herunterladen_mit_http(package_name, url)
    elif type is 2:
        klon_mit_git(package_name, url)
    elif type is 3:
        klon_mit_subversion(package_name, url)
    else:
        print("FEHLER: ändern fehler")


def finden_art(package_name):
    ftp_list = [line.rstrip('\n') for line in open("FTPindex")]
    for i in ftp_list:
        if i == package_name:
            return 0
    http_list = [line.rstrip('\n') for line in open("HTTPindex")]
    for iter in http_list:
        if iter == package_name:
            return 1
    git_list = [line.rstrip('\n') for line in open("GITindex")]
    for iterate in git_list:
        if iterate == package_name:
            return 2
    subversion_list = [line.rstrip('\n') for line in open("SUBVERSIONlist")]
    for iteration in subversion_list:
        if iteration == package_name:
            return 3
    return 4


def ueberpruefung_package(package_name):
    lines = [line.rstrip('\n') for line in open("packages")]
    for i in lines:
        if i == package_name:
            return True
    return False


def main():
    a = argparse.ArgumentParser(description="a package manager for *nix")
    a.add_argument('package', type=str, help='the package you want to install')
    args = a.parse_args()
    package_name = args.package
    if ueberpruefung_package(package_name):
        type = finden_art(package_name)
        if type is 0:
            herunterladen_package(0, package_name)
        elif type is 1:
            herunterladen_package(1, package_name)
        elif type is 2:
            herunterladen_package(2, package_name)
        elif type is 3:
            herunterladen_package(3, package_name)
        else:
            print("FEHLER: Kann nicht herunterladen datei")
            exit(0)
    else:
        print("jetzt Datei ist nicht verfügbar, bitte versuchen nochmals später")


main()
