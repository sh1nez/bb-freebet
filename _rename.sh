sed -i "s/USERNAME/$1" startup.sh
sed -i "s/USERNAME/$1" freebet.sh
mv freeebet.service /etc/systemd/system/"$1"freebet.service
systemctl enable --now "$1"freebet.service
