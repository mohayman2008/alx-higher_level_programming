#!/usr/bin/node
// The script write a string to a file
//  1st Arg: The file path
//  2nd Arg: the string to be written to the file

const argv = process.argv;
const fs = require('fs');

const path = argv[2];
const contents = argv[3];

fs.writeFile(path, contents, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
