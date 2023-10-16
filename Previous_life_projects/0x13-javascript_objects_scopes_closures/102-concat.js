#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

const in1 = argv[2];
const in2 = argv[3];
const out = argv[4];

const content = fs.readFileSync(in1) + fs.readFileSync(in2);

fs.writeFileSync(out, content);
