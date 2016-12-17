#!/usr/bin/env python3
import argparse
import os
import requests
import subprocess
import tarfile
import urllib
import zipfile

os = os.name


def create_file_name(url):  # Takes the file name from the url so it can be correctly extracted
    for i in range(len(url) - 1, -1, -1):
        if url[i] == '/':
            return url[i + 1:]


def find_type_and_unzip():
    file_name, file_extention = os.path.splitext("packageName")
    if file_extention is ".zip" or file_extention is '.gzip':
        # File is a zip
        fileHandle = open('packageFile', 'rb')
        zipfile.ZipFile("packageName").extractall()

    elif file_extention is '.tar' or file_extention is '.tar.gz':
        # File is either a tar or tar.gz and can be extracted with 'tar'
        tar = tarfile.open("packageFile")
        tar.extractall()
    else:
        print("File extension not recognized ")


def unzip_file(archive_type):  # NOTE: 0 = zip / 1 = tar
    if archive_type is 0:
        zipfile.ZipFile("packageFile").extractall()
    elif archive_type is 1:
        tarfile.TarFile('packageFile').extractall()
    else:
        print("type pass failed")


def configure_source(source_type, compile_arguments):
    if source_type is 0 or source_type is 10 and "posix" in os:  # os.name returns 'posix' on OSX systems
        subprocess_arguments = ('sudo', './configure')
        process = subprocess.Popen(subprocess_arguments, stdout=subprocess.PIPE)
        print("Configuring...")
        output = process.stdout.read()
        print(output)
    else:
        print('source type not recognized')


def compile_source_if_necessary(source_type, compile_arguments):  # compileCommands can be left null if not necessary
    # NOTE: 0 = make (gnu) "sudo make install"
    if compile_arguments is not None:
        if source_type == 0:
            subprocess_arguments = ('sudo', 'make', 'install', 'packageFile')
            process = subprocess.Popen(subprocess_arguments, stdout=subprocess.PIPE)
            print('compiling')
            print('output...')
            process.wait()
            output = process.stdout.read()
            print(output)

        else:
            print("Not recognized compile type passed as sourceType")


def ftp_download(url):
    urllib.urlretrieve(url, create_file_name(url))
    print 'hello'
    # NOTE: url must be prefixed with ftp://


def http_download(package_name, url):
    requests.get(url, 'packageFile')
    # NOTE: url must be prefixed with http:// or https://


def git_download(package_name, url):
    urllib.urlretrieve(url, 'packageFile')
    # NOTE url must be prefixed with git://


def subversion_download(package_name, url):
    urllib.urlretrieve(url, 'packageFile')
    # NOTE url must be prefixed with subverion prefix


def download_package(type, package_name):
    index = 0
    lines = [line.rstrip('\n') for line in open("packages")]
    for i in range(0, len(lines)):
        if lines[i] == package_name:
            index = i
            break
    url_lines = [line.rstrip('\n') for line in open("packageURL")]
    url = url_lines[index]
    if type == 0:
        ftp_download(url)
    elif type is 1:
        http_download(package_name, url)
    elif type is 2:
        git_download(package_name, url)
    elif type is 3:
        subversion_download(package_name, url)
    else:
        print("ERROR: download function could not be run for an unknown reason")


def check_type(package_name):
    ftp_list = [line.rstrip('\n') for line in open("FTPindex")]
    for i in ftp_list:
        if i == package_name:
            return 0
    http_list = [line.rstrip('\n') for line in open("HTTPindex")]
    for iter in http_list:
        if iter is package_name:
            return 1
    git_list = [line.rstrip('\n') for line in open("GITindex")]
    for iterate in git_list:
        if iterate is package_name:
            return 2
    subversion_list = [line.rstrip('\n') for line in open("SUBVERSIONlist")]
    for iteration in subversion_list:
        if (iteration is package_name):
            return 3
    return 4


def verify_package(package_name):
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
    if verify_package(package_name):
        type = check_type(package_name)
        if type is 0:
            download_package(0, package_name)
        elif type is 1:
            download_package(1, package_name)
        elif type is 2:
            download_package(2, package_name)
        elif type is 3:
            download_package(3, package_name)
        else:
            print("Error: package download method could not be found")
            exit(0)
    else:
        print("Package not available at this time or could not be verified, sorry :( ")


main()
