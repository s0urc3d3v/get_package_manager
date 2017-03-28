#!/usr/bin/env bash
# Dies skipt läft von get_package_manager Ordner weil subproccess dingen
cd Python-3.5.2
touch ../out/configure_out.txt
touch ../out/make_out.txt
touch ../out/make_install_out.txt
./configure >> ../out/configure_out.txt
make >> ../out/make_out.txt
make >> ../out/make_install_out.txt
