#!/usr/bin/node
// The script gets the contents of a webpage and stores it in a file
//  1st Arg: The URL of the webpage
//  2nd Arg: The file path

const argv = process.argv;
const request = require('request');
const fs = require('fs');

const url = argv[2];
const path = argv[3];

// let res;

const errorHandler = function (error) {
  if (error) {
    console.log(error);
  }
};

request({ url: url }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf8', errorHandler);
    // console.log(res);
    // res = body;
    // console.log(res);
  }
});
