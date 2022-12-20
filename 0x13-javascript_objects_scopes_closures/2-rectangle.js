#!/usr/bin/node

module.exports = Rectangle = class Rectangle {
  constructor (w, h) {
    if (w && h && Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
