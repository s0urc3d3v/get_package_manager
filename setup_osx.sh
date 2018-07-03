#!/usr/bin/env bash
echo "Vor diese Anwendung ausfueren koennen, muessen Sie, voraussetzung paket installieren\nDies Anwendung installieren \"xcode tools\" und \"homebrew\" dann \"wget\" durch homebrew \n Es ist eine moerchlichkeiten mehr werden installiert durch homebrew, falls es ist boenertigt"
echo "Fortfahren? [y,n]"
read weiter
if [[ "$weiter" == "y" ]]; then
    xcode-select --install
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    brew install wget
else
    echo "Installieren abbrechen"
fi