#!/usr/bin/env bash
# Dies skipt läft von get_package_manager Ordner weil subproccess dingen
cd Python-3.5.2
./configure
make
make install
