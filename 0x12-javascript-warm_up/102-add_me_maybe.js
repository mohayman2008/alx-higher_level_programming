#!/usr/bin/node

// exports.addMeMaybe = function (x, func.bind(this, num + 1))
exports.addMeMaybe = function (x, func) {
  func();
};
