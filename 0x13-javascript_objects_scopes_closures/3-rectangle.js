#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let item = 0; item < this.height; item++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
