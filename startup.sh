#!/usr/bin/env bash

user=freebeter
active_dir=/home/freebeter/bb-freebet
client_dir="$active_dir"/profiles

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
python "$active_dir"/main.py "${array[@]}" &

#clients
cnt=0
for i in "${clients[@]}"; do
	su -c "python3 $active_dir/main.py $i/profile ${array[cnt]}" "$user" &
	((cnt+=1))
done
