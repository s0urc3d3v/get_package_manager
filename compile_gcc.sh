#!/usr/bin/env bash
./contrib/download_prerequisites
cd gcc-4.6.2
mkdir out
cd out
$PWD/../gcc-4.6.2/configure --prefix=$HOME/gcc-4.6.2 --enable-languages=c,c++,fortran,go
make
make install