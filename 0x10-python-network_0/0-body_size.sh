#!/bin/bash

# This script sends a request to a URL and displays the size of the body of the response.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')
echo "$size"
