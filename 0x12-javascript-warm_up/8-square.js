#!/usr/bin/node

const argv = process.argv;

let out = '';
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(argv[2]);
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      out += 'X';
    }
    if (i < size - 1) {
      out += '\n';
    }
  }
  if (size > 0) {
    console.log(out);
  }
}
