#!/bin/bash
# This script sends a request to a URL passed in as an argument, and displays only the status code of the response
curl -sw '%{http_code}' -o /dev/null "$1"
