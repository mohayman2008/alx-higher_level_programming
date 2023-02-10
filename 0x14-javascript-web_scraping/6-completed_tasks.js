#!/usr/bin/node
// The script computes the number of tasks completed by each employee referred by their <id>s
//  1st Arg: The API URL "https://jsonplaceholder.typicode.com/todos"

const argv = process.argv;
const request = require('request');

const url = argv[2];

request({ url: url }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resp = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (resp[json[i].userId] === undefined) {
          resp[json[i].userId] = 0;
        }
        resp[json[i].userId]++;
      }
    }
    console.log(resp);
  }
});
