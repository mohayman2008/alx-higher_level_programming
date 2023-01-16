#!/bin/bash
# This script sends an 'OPTIONS' request to a URL passed in as an argument and displays the allowed request methods
curl -sIX 'OPTIONS' "$1" | grep 'Allow:' | cut -f 2- -d' '
