#!/bin/bash
# Script that takes a URL, sends a GET request, and displays the body of the response

curl -s "$1" -X GET -i | grep -i Content-Length | awk '{print $2}'
