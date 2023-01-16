#!/bin/bash
# This script sends a 'POST' request with queries to a URL passed in as an argument and displays the body of the response
curl -s -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"
