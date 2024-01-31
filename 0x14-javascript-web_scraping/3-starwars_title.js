#!/usr/bin/node
// The script prints the title of a Star Wars movie
// where the episode number passed as an argument

const argv = process.argv;
const request = require('request');

const id = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request({ url: url }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      const filmData = JSON.parse(body);
      console.log(filmData.title);
    } catch (err) {
      console.log('Not a valid JSON was received');
    }
  }
});
