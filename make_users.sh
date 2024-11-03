#!/usr/bin/env bash


for i in $(find "/home" -maxdepth 1 -mindepth 1 -type d); do
    rm -r "$i"/bb-freebet/
    mkdir -p "$i"/bb-freebet/profile
    cp -r /usr/local/src/bb-freebet/client/* "$i/bb-freebet/"
    cp -r /usr/local/profiles${i/\/home/}/* "$i"/bb-freebet/profile
    cd "$i/bb-freebet/"
    bash start.sh
done

systemctl restart parser.service
