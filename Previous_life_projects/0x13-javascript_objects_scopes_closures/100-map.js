#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map(function (idx, num) {
  return idx * num;
});

console.log(list);
console.log(newList);
