#!/bin/bash

SERVER_IMAGE="$1"
SERVER_PORT="$2"


echo "Check start server container"
if docker ps | grep "$SERVER_IMAGE" > /dev/null; then
    echo "###### Server is up! ######"
else
    echo "###### Server container is down! ######"
    exit 1
fi

echo "Check open port"
if ss -tulpn | grep "$SERVER_PORT" > /dev/null; then
    echo "###### Server port is open! ######"
else
    echo "###### Server port is closed! ######"
    exit 1
fi
