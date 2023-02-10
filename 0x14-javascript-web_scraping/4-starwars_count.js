#!/usr/bin/node
// The script prints the number of movies where the character “Wedge Antilles” is present
// The first argument is the API URL of the Star wars API "https://swapi-api.alx-tools.com/api/films/"

const argv = process.argv;
const request = require('request');

const url = argv[2].slice(0, argv[2].search('/films')) + '/people/18';

request({ url: url }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      const charData = JSON.parse(body);
      console.log(charData.films.length);
    } catch (err) {
      console.log('Not a valid JSON was received');
    }
  }
});
