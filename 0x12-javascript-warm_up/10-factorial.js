#!/usr/bin/node

const argv = process.argv;

function factorial (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(argv[2]));
