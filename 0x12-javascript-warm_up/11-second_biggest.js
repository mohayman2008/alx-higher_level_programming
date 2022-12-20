#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.sort(function (a, b) {a - b})
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
