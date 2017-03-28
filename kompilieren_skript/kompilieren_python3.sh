#!/usr/bin/env bash
# Dies skipt läft von get_package_manager Ordner weil subproccess dingen
cd Python-3.5.2
touch ../ausgebe/configure_out.txt
touch ../ausgebe/make_out.txt
touch ../ausgebe/make_install_out.txt
echo "macht ist fast getstartet.  Die ausgebe ist im die ausgebe ordner.  Warnung: Das wird lange dauern!"
./configure >> ../ausgebe/configure_out.txt
make >> ../ausgebe/make_out.txt
make install >> ../ausgebe/make_install_out.txt
read -n1 -p "Löschen ausgebe datei? (J/N)", loeschen
if [[ $loeschen == "J" || $loeschen == "j" ]]; then
    rm -rf ../ausgebe/make_out.txt
    rm -rf ../ausgebe/make_install_out.txt
    rm -rf ../ausgebe/configure_out.txt
    echo "Ausgebe gelöscht ist"
else
    echo "Ausgebe gespeichert ist"
fi