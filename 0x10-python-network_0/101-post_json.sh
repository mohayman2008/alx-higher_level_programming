#!/bin/bash
# This script ends a JSON POST request to a URL passed in as an argument and displays the body of the response
curl -s -X 'POST' -H "Content-Type: application/json" -d '@'"$2" "$1"
