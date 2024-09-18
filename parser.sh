#!/usr/bin/env bash

active_dir=/usr/local/src/bb-freebet

mapfile -t clients < <(find "/home" -maxdepth 1 -mindepth 1 -type d)

len=${#clients[@]}

array=()
port=44000
cnt=0
while [ $port -le 65535 ] && [ $cnt -lt "$len" ]; do
	if ! ss -tuln | grep "$port"; then
		array+=("$port")
		((cnt+=1))
	fi
	((port+=1))
done


for (( i=0; i<len; ++i)); do
	echo "${array[$i]}" > "${clients[$i]}"/bb-freebet/socket.txt
done

for dir in /home/*; do
	systemctl restart "$(basename "$dir")freebet.service"
done

echo "$active_dir"/main.py "${array[@]}"
source "$active_dir"/venv/bin/activate
python3 "$active_dir"/main.py "${array[@]}"
