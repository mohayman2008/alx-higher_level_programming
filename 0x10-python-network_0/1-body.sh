#!/bin/bash
# This script sends a request to a URL passed in as an argument, follows redirections and displays the body of the response
curl -sL "$1"
