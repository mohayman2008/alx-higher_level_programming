#!/usr/bin/node
// The script prints all the characters of a Star Wars movie
// where the episode number passed as an argument

const argv = process.argv;
const request = require('request');
const url = require('url');

const id = argv[2];
const URL = new url.URL(`https://swapi-api.alx-tools.com/api/films/${id}`);

async function errorHandler (error) {
  if (error) {
    console.log(error);
  }
}

function getBodyPromise (options) {
  return new Promise(function (resolve, reject) {
    request(options, (error, response, body) => {
      resolve(body);
      reject(error);
    });
  });
}

async function printChars (error, response, body) {
  if (error) {
    errorHandler(error);
  } else {
    // body should be an object
    const chars = body.characters;
    for (const char of chars) {
      const charURL = new url.URL(char);
      const options = { url: charURL, json: true };
      const charObj = await getBodyPromise(options);
      console.log(charObj.name);
    }
  }
}

request({ url: URL, json: true }, printChars);
