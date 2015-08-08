#!/usr/bin/env python3
import argparse, urllib, requests


def ftp_download(package, url):
    urllib.urlretrieve(url, 'packageFile')
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
    for i in lines:
        if (i == package_name):
            index = i
            break
    URLlines = [line.rstrip('\n') for line in open("packageURL")]
    url = URLlines[index]
    if (type is 0):
        ftp_download(package_name, url)
    elif (type is 1):
        http_download(package_name, url)
    elif (type is 2):
        git_download(package_name, url)
    elif(type is 3):
        subversion_download(package_name, url)
    else:
        print("ERROR: download function could not be run for an unknown reason")


def check_type(package_name):
    FTPList = [line.rstrip('\n') for line in open("FTPindex")]
    for i in FTPList:
        if (i is package_name):
            return 0
    HTTPList = [line.rstrip('\n') for line in open("HTTPindex")]
    for iter in HTTPList:
        if (iter is package_name):
            return 1
    GITlist = [line.rstrip('\n') for line in open("GITindex")]
    for iterate in GITlist:
        if (iterate is package_name):
            return 2
    SUBVERSIONlist = [line.rstrip('\n') for line in open("SUBVERSIONlist")]
    for iteration in SUBVERSIONlist:
        if (iteration is package_name):
            return 3
    return 4


def verify_package(package_name):
    lines = [line.rstrip('\n') for line in open("packages")]
    for i in lines:
        if (i is package_name):
            return True
    return False


def main():
    a = argparse.ArgumentParser(description="a package manager for *nix")
    a.add_argument('package', type=str, help='the package you want to install')
    args = a.parse_args()
    package_name = args.package
    if verify_package(package_name):
        type = check_type(package_name)
        if (type is 0):
            download_package(0, package_name)
        elif (type is 1):
            download_package(1, package_name)
        elif (type is 2):
            download_package(2, package_name)
        elif (type is 3):
            download_package(3, package_name)
        else:
            print("Error: package download method could not be found")
            exit(0)
    else:
        print("Package not available at this time or could not be verified, sorry :( ")


main()
