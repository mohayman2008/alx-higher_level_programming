#!/usr/bin/node
// The script gets the contents of a webpage and stores it in a file
//  1st Arg: The URL of the webpage
//  2nd Arg: The file path

const argv = process.argv;
const request = require('request');
const fs = require('fs');
const url = require('url');

const URL = new url.URL(argv[2]);
const path = argv[3];

function errorHandler (error) {
  if (error) {
    console.log(error);
  }
}

function reqHandler (error, response, body) {
  if (error) {
    errorHandler(error);
  } else {
    fs.writeFile(path, body, 'utf8', errorHandler);
  }
}

request({ url: URL }, reqHandler);
