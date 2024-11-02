#!/usr/bin/env bash


for i in $(find "/home" -maxdepth 1 -mindepth 1 -type d); do
    mkdir "$i"/bb-freebet/
    cp -r /usr/local/profiles${i/\/home/} "$i"/bb-freebet/
    cp -r client/* "$i/bb-freebet/"
    cd "$i/bb-freebet/"
    bash start.sh
done
