#!/usr/bin/node

const SquareParent = require('./5-square') //call the parent

class Square extends SquareParent {
  constructor (size) {
    super(size);
  }
  charPrint (c) {
    if (c === undefined) {
      c = 'X'
    }

    for (let item = 0; item < this.height; item++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
