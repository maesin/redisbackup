# redisbackup
## Installation
```bash
pip install -U -e git+ssh://git@github.com/maesin/redisbackup.git@master#egg=redisbackup-0.0.0
```

## Usage
### Command line
```bash
redisbackup --interval 3600 --port 6379 --copy /path/to/copy.rdb
```

### Python module
```bash
>>> import redisbackup
>>> redisbackup.backup(port=6379, copy='/path/to/copy.rdb')
```

## Daemon Setup
### Systemd
```bash
sudo cp redisbackup.service /etc/systemd/system/redisbackup.service
```

### Init script
```bash
sudo cp redisbackup.update-rc.d.init.sh /etc/init.d/redisbackup
```
