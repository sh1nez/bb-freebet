#!/usr/bin/env bash

user=freebeter
active_dir=/home/"$user"/bb-freebet
client_dir="$active_dir"/profiles

rm "$active_dir"/log*.txt
# chown -R $user:$user "$active_dir"

# clients=$(find "$client_dir" -maxdepth 1 -type d)
mapfile -t clients < <(find "$client_dir" -maxdepth 1 -mindepth 1 -type d)

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
#
# server
source "$active_dir"/venv/bin/activate
echo "$active_dir"/main.py "${array[@]}"
python3 "$active_dir"/main.py "${array[@]}" &

#clients
cnt=0
for i in "${clients[@]}"; do
	echo "python3 $active_dir/chrome.py $i ${array[cnt]}"
	su -c "python3 $active_dir/chrome.py $i ${array[cnt]}" "$user" &
	((cnt+=1))
done
