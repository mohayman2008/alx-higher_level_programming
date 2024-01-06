#!/bin/bash
# This script sends a request to a URL passed in as an argument, and displays the size of the body of the response
curl -sw '%{size_download}\n' -o /dev/null "$1"
