#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let item = 0; item < this.height; item++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
