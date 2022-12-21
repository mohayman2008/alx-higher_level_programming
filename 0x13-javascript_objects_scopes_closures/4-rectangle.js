#!/usr/bin/node

const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w && h && Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.height || !this.width) {
      return;
    }

    let out = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        out += 'X';
      }
      if (i < this.height - 1) {
        out += '\n';
      }
    }
    console.log(out);
  }

  rotate () {
    if (!this.height || !this.width) {
      return;
    } const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    if (!this.height || !this.width) {
      return;
    }
    this.width *= 2;
    this.height *= 2;
  }
};

module.exports = Rectangle;
