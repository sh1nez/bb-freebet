user=$(pwd | awk -F'/' '{print $3}')

if [ ! -d venv ]; then
	python3 -m venv venv
fi
venv/bin/pip3 install -r requirements.txt

sed -i "s/USERNAME/$user/g" freebet.service
sed -i "s/USERNAME/$user/g" chrome.py

cp freebet.service /etc/systemd/system/"$user"freebet.service

chown -R ${user}:${user} /home/${user}/

systemctl daemon-reload

systemctl enable --now "$user"freebet.service
