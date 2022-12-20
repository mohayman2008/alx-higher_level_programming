#!/usr/bin/node

const argv = process.argv;

if (argv.length < 4) {
  console.log(0);
} else {
  console.log(argv.slice(2).sort(function (a, b) {
    return (Number(b) - Number(a));
  })[1]);
}
