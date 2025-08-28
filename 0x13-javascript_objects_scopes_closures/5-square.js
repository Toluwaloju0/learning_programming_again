#!/usr/bin/node

/**
 * a method to create a class that extends from another
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (val) {
    /**
     * the constructor method it takes one argument which is the width of the square
     */
    super(val, val);
  }
}

module.exports = Square;
