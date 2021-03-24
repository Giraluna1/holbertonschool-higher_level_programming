#!/usr/bin/node
const Rectangle = require('./4-rectangle'); //Import the parent

class Square extends Rectangle {
  constructor (size) {
    super(size, size); //call th super class constructor
  }
}

module.exports = Square;
