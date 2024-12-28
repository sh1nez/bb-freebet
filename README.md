# BetBoom freebet multi farmer

## installisation guide:
- Clone git repository
```bash
mkdir -p /usr/local/src/
cd /usr/local/src/
git clone git@github.com:sh1nez/bb-freebet.git
```

- copy all google chrome profiles
```bash
mkdir -p /usr/local/profiles
cp '/path/to/profiles/' /usr/local/
```

- make users for all profiles
```bash
./make_users.sh
```
- install services
```bash
./start.sh
```

- start service
```bash
./parser.sh
```

##### If you need to have users without a bb client, enter them manually in the parser.sh files
