#!/usr/bin/env bash
cd ..
cd
./configure --prefix=~/python-2.7.3 --enable-shared
make
make install
