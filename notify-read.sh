#!/usr/bin/bash

DIR_CACHE="$HOME/.cache"
DIR_LOCAL="$HOME/.local"
DIR_BIN="$DIR_LOCAL/bin"

# notify-read -n items -a "appname"
# to get last or now playing track: notify-read -n1 -a "spotify" 

app="networkmanager"
items=180

while getopts a:t:n: flag
do
    case "${flag}" in
        a) app=${OPTARG};;
        n) items=${OPTARG};;
    esac
done


LINES=$(grep -i "${app}" $DIR_CACHE/notifications.log | uniq | tail -n $items)
echo "------------------------------------------------------------------------------------------"

while read -r LINE
do
    while IFS='::' read -ra N; do
        n_date=$(date --date @"${N[0]}" +"%F")
        n_time=$(date --date @"${N[0]}" +"%T")
        n_title="${N[4]}"
        n_description="${N[6]}"
        
        echo -e "Title:${n_title}\nDescription:${n_description}\nDate:${n_date}\nTime:${n_time}"
        
    done <<< "$LINE"
    echo "------------------------------------------------------------------------------------------"
done <<< "$LINES"

