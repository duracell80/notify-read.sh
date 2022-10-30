#!/usr/bin/bash

DIR_CACHE="$HOME/.cache"
DIR_LOCAL="$HOME/.local"
DIR_BIN="$DIR_LOCAL/bin"

# KILL PREVIOUS INSTANCES
PID_CURR=$$
PID_COUNT=$(ps aux | grep "notify-watch.sh" | head -n -1 | wc -l)

if [[ "$PID_COUNT" > 1 ]]; then
    PID_PREV=$(ps aux | grep "notify-watch.sh" | head -n -1 | head -n 1 | awk '{print $2}')
    if [[ "$PID_PREV" -ne "$PID_CURR" ]]; then
        kill $PID_PREV
    fi
fi



# CLEANUP LOG FILE OF ENTRIES OLDER THAN 30 DAYS
current_timestamp=$(date +%s)
while read line; do
    set -- ${line/::/ }
    
    timestamp=$1
    appname=$2
    title=$3
    description=$4
    
    ((diff = current_timestamp - timestamp))
    if ((diff >= 2592000)); then
        sed -i "/^$timestamp:/d" $DIR_CACHE/test.log.tmp
    fi
done < $DIR_CACHE/notifications.log

# RUN THE READ WORKER
$DIR_BIN/notify-read.py &