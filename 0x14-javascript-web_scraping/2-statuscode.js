#!/usr/bin/node
// The script displays the status code of a GET request

const argv = process.argv;
const request = require('request');

const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
