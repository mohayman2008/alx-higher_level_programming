#!/bin/bash
# This script sends a request to that URL passed in as an argument, and displays the size of the body of the response
curl -sIX 'OPTIONS' "$1" | grep 'Allow:' | cut -f 2- -d' '
