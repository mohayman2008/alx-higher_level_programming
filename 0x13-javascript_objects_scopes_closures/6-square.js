#!/usr/bin/node

const ParentSquare = require('./5-square');

const Square = class Square extends ParentSquare {
  /* constructor (size) {
    super(size);
  } */

  charPrint (c) {
    if (!this.height || !this.width) {
      return;
    }
    let chr;
    if (c) {
      chr = c;
    } else { chr = 'X'; }

    let out = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        out += chr;
      }
      if (i < this.height - 1) {
        out += '\n';
      }
    }
    console.log(out);
  }
};

module.exports = Square;
