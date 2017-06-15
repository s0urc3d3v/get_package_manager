#!/usr/bin/env bash
# %1 namen von datei
# %2 configure befehl;
cd $1
touch ../ausgebe/configure_out.txt
touch ../ausgebe/make_out.txt
touch ../ausgebe/make_install_out.txt
echo "Bauen ist fast begonnen. Die ausgebe ist im ausgebe ordner.  Warnung das wird lange dauern!"
./$2>> ../ausgebe/make.txt
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