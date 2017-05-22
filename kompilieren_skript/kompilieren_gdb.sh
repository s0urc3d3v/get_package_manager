#!/usr/bin/env bash
cd gdb-7.12
touch ../ausgebe/configure_out.txt
touch ../ausgebe/make_out.txt
touch ../ausgebe/make_install_out.txt
echo "Bauen ist fast begonnen. Die ausgebe ist im ausgebe ordner.  Warnung das wird lange dauern!"
./configure --prefix=/usr --with-system-readline --without-guile>> ../ausgebe/make.txt
make >> ../ausgebe/make_out.txt
make install >> ../ausgebe/make_install_out.txt
echo "Loeschen ausgebe datei? (J/N)"
read loeschen
if [[ $loeschen == "J" || $loeschen == "j" ]]; then
    rm -rf ../ausgebe/make_out.txt
    rm -rf ../ausgebe/make_install_out.txt
    rm -rf ../ausgebe/configure_out.txt
    echo "Ausgebe gelöscht ist"
else
    echo "Ausgebe gespeicgert ist"
fi
exit