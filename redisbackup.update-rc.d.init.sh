#!/bin/sh
# Provides: redisbackup
# Required-Start: $syslog $remote_fs bootlogs
# Required-Stop: $syslog $remote_fs
# Should-Start: $local_fs
# Should-Stop: $local_fs
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6

EXEC=/path/to/venv/bin/redisbackup --interval 3600 --port 6379 --copy /path/to/copy.rdb
PIDFILE=/var/run/redisbackup.pid

case "$1" in
    start)
        if [ -f $PIDFILE ]
        then
                echo "$PIDFILE exists, process is already running or crashed"
        else
                echo "Starting Redisbackup..."
                $EXEC
        fi
        ;;
    stop)
        if [ ! -f $PIDFILE ]
        then
                echo "$PIDFILE does not exist, process is not running"
        else
                PID=$(cat $PIDFILE)
                echo "Stopping ..."
                kill $PID
                while [ -x /proc/${PID} ]
                do
                    echo "Waiting for Redisbackup to shutdown ..."
                    sleep 1
                done
                echo "Redisbackup stopped"
        fi
        ;;
    *)
        echo "Please use start or stop as first argument"
        ;;
esac