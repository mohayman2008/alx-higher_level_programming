#!/usr/bin/node
// The script prints the number of movies where the character “Wedge Antilles” is present
// The first argument is the API URL of the Star wars API "https://swapi-api.alx-tools.com/api/films/"

const argv = process.argv;
const request = require('request');

const url = argv[2];
const charUrl = 'people/18';

request({ url: url }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      const films = JSON.parse(body).results;

      let count = 0;
      for (const film of films) {
        const chars = film.characters;
        for (const char of chars) {
          if (char.indexOf(charUrl) !== -1) {
            count++;
            break;
          }
        }
      }
      console.log(count);
    } catch (err) {
      console.log('Not a valid JSON was received');
    }
  }
});
