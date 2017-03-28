#!/usr/bin/env bash
cd gcc*
./contrib/download_prerequisites
cd ausgebe
DIR_NAME=${PWD##*/}
./configure --enable-languages=c,c++,fortran,go
make
make install