#!/usr/bin/env bash
cd gcc*
./contrib/download_prerequisites
mkdir out
cd out
DIR_NAME=${PWD##*/}
./configure --enable-languages=c,c++,fortran,go
make
make install