#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import platform
import subprocess
import tarfile
import urllib
import zipfile
import clint
from clint.textui import progress
import requests
from os.path import expanduser
from pathlib import Path
import contextlib
import csv

os_name = os.name
jetzt_datei_namen = ''
source_path = ''
herunterladen_datei_namen = ''


def aktuell_datei():
    url_packages = 'https://raw.githubusercontent.com/s0urc3d3v3l0pm3nt/get_package_manager/master/packages'
    url_ftp = 'https://raw.githubusercontent.com/s0urc3d3v3l0pm3nt/get_package_manager/master/FTPindex'
    url_git = 'https://raw.githubusercontent.com/s0urc3d3v3l0pm3nt/get_package_manager/master/GITindex'
    url_http = 'https://raw.githubusercontent.com/s0urc3d3v3l0pm3nt/get_package_manager/master/HTTPindex'
    url_subversion = 'https://raw.githubusercontent.com/s0urc3d3v3l0pm3nt/get_package_manager/master/SUBVERSIONlist'

    url_liste = [url_packages, url_ftp, url_git, url_http, url_subversion]

    for geganwaertig in url_liste:
        nchste = 0
        for buchstube in range(0, len(geganwaertig)):
            if geganwaertig[buchstube] == '/':
                nchste = buchstube + 1
        aktuell_datei_namen = geganwaertig[nchste: len(geganwaertig)]
        verbindung = requests.get(geganwaertig)
        datei = open(aktuell_datei_namen, 'r+')
        datei.write(verbindung.content)
    print('Alles aktuell. Viel glück!')


def loeschen_herunterladen_datei():
    print 'hello'
    #  müsst hinzufügen die herunterladen_datei_namen für diesen dingen


def automatisch_konfigurieren():
    print ""
    # lesen aus datei zu finden arguments und datei namen aus method


def anrufen_skipt_mit_argumente(datei_namen_ohne_erweiterung,
                                configure):  # ändern function behaltet aber neuer function werden benutzten diesen function
    process = os.popen("./kompilieren_skript/Global_skript.sh %s %s" % (datei_namen_ohne_erweiterung, configure))


def anrufen_skipt(skript_pfad):
    path = os.getcwd() + "/kompilieren_skript/" + skript_pfad
    subprocess.call(path, shell=True)


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


def shaffen_datei_namen(url):  # Die namen bekommt aus die datei für entpack
    for i in range(len(url) - 1, -1, -1):
        if url[i] == '/':
            return url[i + 1:]


def finden_art_und_entpack():
    dateiweiterung = ''
    for i in range(0, len(jetzt_datei_namen)):
        if jetzt_datei_namen[i] == '.':
            if not ((jetzt_datei_namen[i + 1]).isdigit() and (jetzt_datei_namen[i - 1]).isdigit()):
                dateiweiterung = jetzt_datei_namen[i:]
                break
    if dateiweiterung == '':
        print('Datei ist korrupt, tut mir leid')
    if dateiweiterung == ".zip" or dateiweiterung == '.gzip':
        # Zip
        fileHandle = open('packageFile', 'rb')
        zipfile.ZipFile("packageName").extractall()

    elif dateiweiterung == '.tar' or dateiweiterung == '.tar.gz' or dateiweiterung == '.tgz' or dateiweiterung == '.tar.xz':
        #  Datei ist eine 'tar'. .tar.xz Datei sind nicht fertig.
        tar = tarfile.open(jetzt_datei_namen)
        tar.extractall()
        tar.close()
        kopilieren_code_fall_benoetigt()
    # elif dateiweiterung == '.tgz':
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


def konfigurieren_code(source_type, kompiliern_streit):
    if source_type is 0 or source_type is 10 and "posix" in os:  # os.name returns 'posix' on OSX systems
        subprocess_arguments = ('sudo', './configure')
        process = subprocess.Popen(subprocess_arguments, stdout=subprocess.PIPE)
        print("Configuring...")
        output = process.stdout.read()
        print(output)
    else:
        print('source type not recognized')


def kopilieren_code_fall_benoetigt():
    for n in range(0, len(jetzt_datei_namen)):
        if jetzt_datei_namen[n] == '-':
            Version = jetzt_datei_namen[n + 1:n + 2]
            break
    if Version.isdigit() == False:
        print "Keine Version gefunden"
    if ('Python' in jetzt_datei_namen) and ('2' in Version):  # Python 2
        print('Nicht Umgesetzt wurden noch')
    elif ('Python' in jetzt_datei_namen) and ('3' in Version):  # Python 3
        anrufen_skipt('kompilieren_python3.sh')  # Ich kennt dies können besser gemacht
    elif 'gcc' in jetzt_datei_namen:
        anrufen_skipt('kompilieren_gcc.sh')
    elif 'gdb' in jetzt_datei_namen:
        anrufen_skipt_mit_argumente(jetzt_datei_namen, "configure")
    else:
        automatisch_konfigurieren()


def herunterladen_mit_ftp(url):
    global jetzt_datei_namen  # bekommen var Berichtigungen
    jetzt_datei_namen = shaffen_datei_namen(url)
    source_exists = os.path.exists(os.path.abspath(jetzt_datei_namen))
    if not source_exists:  # prüfung ob datei existiert
        urllib.urlretrieve(url, jetzt_datei_namen)
    finden_art_und_entpack()
    kopilieren_code_fall_benoetigt()
    # NOTE: url müsst mit ftp:// begonnen


def herunterladen_mit_http(package_name, url):
    global jetzt_datei_namen  # bekommen var Berichtigungen
    jetzt_datei_namen = shaffen_datei_namen(url)  # Dies müsst in alles herunterladen methoden sein!
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




    # Achtung: url müsst begonnen http:// or https:// mit


def klon_mit_git(package_name, url):
    urllib.urlretrieve(url, 'packageFile')
    # NOTE url müsst begonnen git:// mit


def klon_mit_subversion(package_name, url):
    urllib.urlretrieve(url, 'packageFile')
    # NOTE url müsst begonnensubverion mit


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

# 0 = FTP
# 1 = HTTP
# 2 = GIT
# 3 - SUBVERSION
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

def vorInstalliernPaket(package_name):
    paketMitVorInstalliernBenoitigt =""    
    with open("vorInstalliernListe", 'wb') as f:
        paketMitVorInstalliernBenoitigt = f.read()
    if (package_name in paketMitVorInstalliernBenoitigt):
        print ""
        # get all items separted by spaces on the line of the package to be installed


def main():
    # aktüll package datei
    prefsList = []
    preferances = {}
    with open("preferances.tsv", "rb") as prefs:
        fileReader = csv.reader(prefs)
        for item in fileReader:
            prefsList.append(item)
    for pref in prefsList:
        preferances.update({pref[0], pref[1]})
    if((preferances.has_key("setup")) == False):
        system = platform.system()
        if (system == 'Darwin'):
            subprocess.call("./setup_osx.sh")
            with open("preferances.tsv", "rb") as prefs:
                prefFile = csv.writer(prefs)
                prefs.write("setup", "true")
        elif (system.find('Ubuntu') != -1 or system.find('Debian') != -1):
            subprocess.call("setup_linux.sh")
            with open("preferances.tsv", "rb") as prefs:
                prefFile = csv.writer(prefs)
                prefs.write("setup", "true")
            subprocess.call("setup_linux.sh")
        else:
            print('Automatisch installiern nicht unterstuetzung auf dies OS.  Bitte lesen das ausgeben zu finden was benoertigen fuer ausfuehren.  Meisten dies nur \"wget\" werden sein')
    aktuell_datei()
    a = argparse.ArgumentParser(description="Paket Manager für OSX")
    a.add_argument('paket', type=str, help='Das packet Sie wollen')
    args = a.parse_args()
    package_name = args.paket
    if ueberpruefung_package(package_name):
        type = finden_art(package_name)  # hunterladen weg
        check
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
        print("Datei ist nicht verfügbar, bitte versuchen nochmals später")


main()
