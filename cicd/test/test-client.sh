#!/bin/bash

CLIENT_IMAGE="$1"


echo "Check start client container"
if docker ps | grep "$CLIENT_IMAGE" > /dev/null; then
    echo "###### Client is up! ######"
else
    echo "###### Client container is down! ######"
    exit 1
fi

echo "Check exist data file"
if stat /app/client_data/data.csv > /dev/null; then
    echo "###### File exist! ######"
else
    echo "###### File does not exist! ######"
    exit 1
fi