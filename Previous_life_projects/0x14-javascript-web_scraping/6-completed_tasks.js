#!/usr/bin/node
// The script computes the number of tasks completed by each employee referred by their <id>s
//  1st Arg: The API URL "https://jsonplaceholder.typicode.com/todos"

const argv = process.argv;
const request = require('request');

const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const out = {};
    try {
      const todos = JSON.parse(body);
      for (const todo of todos) {
        if (todo.completed) {
          const userId = todo.userId;
          if (out[userId] !== undefined) {
            out[userId] += 1;
          } else {
            out[userId] = 1;
          }
        }
      }

      console.log(out);
    } catch (err) {
      console.log('Not a valid JSON was received');
    }
  }
});
