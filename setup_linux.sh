#!/usr/bin/env bash
echo "Vor diese Anwendung ausfueren koennen, muessen Sie, voraussetzung paket installieren\nDies Anwendung installieren \"wget\" durch apt-get \n Es ist eine moerchlichkeiten mehr werden installiert durch apt, falls es ist boenertigt"
echo "Fortfahren? [y,n]"
read weiter
if [[ "$weiter" == "y" ]]; then
    sudo apt-get install wget
else
    echo "Installieren abbrechen"
fi
