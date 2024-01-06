#!/bin/bash
# This script sends a request with custom header to a URL passed in as an argument and displays the body of the response
curl -sH 'X-School-User-Id: 98' "$1"
