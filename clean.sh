#!/usr/bin/env bash
heir=${PWD##*/}
readarray packages < packages
for ((i = 0; i<${packages}; i++));
do
    rm -rf ${packages[$i]}
done
