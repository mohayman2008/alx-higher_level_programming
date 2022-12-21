#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
for (const [key, val] of Object.entries(dict)) {
  if (typeof newDict[val] === 'undefined') {
    newDict[val] = [];
  }
  newDict[val].push(key);
}

console.log(newDict);
