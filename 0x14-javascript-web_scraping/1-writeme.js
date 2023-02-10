#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

const path = argv[2];
const contents = argv[3];

fs.writeFile(path, contents, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
