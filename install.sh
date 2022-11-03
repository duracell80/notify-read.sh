#!/bin/bash
CWD=$(pwd)

DIR_SYSTD="/etc/systemd/system/"
DIR_CACHE="$HOME/.cache"
DIR_LOCAL="$HOME/.local"
DIR_START="$HOME/.config/autostart"

DIR_BIN="$DIR_LOCAL/bin"
mkdir -p $DIR_BIN

cp -f $CWD/notify-read.py $DIR_BIN
cp -f $CWD/notify-read.sh $DIR_BIN/notify-read
cp -f $CWD/notify-watch.sh $DIR_BIN

chmod u+x $DIR_BIN/notify-read.py
chmod u+x $DIR_BIN/notify-read
chmod u+x $DIR_BIN/notify-watch.sh

cp -f $CWD/notifications.json $DIR_CACHE
touch $DIR_CACHE/notifications.log
chmod u+rw $DIR_CACHE/notifications.json

for filename in $CWD/*.desktop; do
    [ -e "$filename" ] || continue
    file=$(echo $filename | sed -e "s|${CWD}||g")
    
    cp -f $filename $DIR_CACHE/$file.tmp
    sed -i "s|~/|$HOME/|g" $DIR_CACHE/$file.tmp
    mv $DIR_CACHE/$file.tmp $DIR_START/$file
done