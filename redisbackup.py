import os
import redis
import shutil
import subprocess
import time
from datetime import datetime

default_port = 6379


def backup(port=default_port, copy=None):
    print('Executed at', datetime.now().isoformat())
    db = redis.StrictRedis(port=port)
    before = db.lastsave()
    db.bgsave()
    s = datetime.now()

    while before == db.lastsave():
        if 4 <= (datetime.now() - s).seconds:
            print('Timed out waiting for the Redis BGSAVE.')
            exit(1)

    c = db.config_get()
    f = os.path.join(c['dir'], c['dbfilename'])
    print('Save to', f)

    if copy:
        d = os.path.dirname(copy)
        git = os.path.exists(os.path.join(d, '.git'))

        if git:
            if d:
                os.chdir(d)

            subprocess.run(['git', 'reset', '--', '.'])
            subprocess.run(['git', 'checkout', '.'])
            subprocess.run(['git', 'clean', '-fdx'])
            subprocess.run(['git', 'pull'])

        shutil.copy(f, copy)
        print('Copy RDB', f, 'to', copy)

        if git:
            print('Automatically backup using Git.')
            subprocess.run(['git', 'add', os.path.basename(copy)])
            subprocess.run(['git', 'commit', '-m', 'Backup Redis RDB'])
            subprocess.run(['git', 'push'])


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Backup Redis RDB')
    parser.add_argument('--interval', type=int, help='Execution interval')
    parser.add_argument('--port', type=int, default=default_port,
                        help='Redis port')
    parser.add_argument('--copy', help='Copy destination of dump')
    args = parser.parse_args()

    while True:
        backup(args.port, args.copy)

        if args.interval:
            time.sleep(args.interval)
        else:
            break

if __name__ == '__main__':
    main()
