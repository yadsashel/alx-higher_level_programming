#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# sends a request an URL, and displays the size of the body of the response
curl -s "$1" | wc -c
