#!/bin/bash

# This script sends a request to a URL and displays the size of the body of the response.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Sends a request to the URL, retrieves the response, and counts the size of the body in bytes
size=$(curl -s "$1" | wc -c)

# Print the size of the body in bytes
echo "$size"
