#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resp = JSON.parse(body);
    const characters = resp.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
