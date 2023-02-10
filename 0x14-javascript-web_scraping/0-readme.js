#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

const path = argv[2];

fs.readFile(path, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
