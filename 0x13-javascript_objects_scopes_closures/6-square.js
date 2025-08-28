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

  charPrint (c) {
    /**
     * a method to print the square using a character
     */

    if (c === undefined) { this.print(); } else {
      let str = '';
      for (let a = 0; a < this.height; a++) {
        for (let b = 0; b < this.width; b++) { str += c; }
        str += '\n';
      }
      console.log(str.slice(0, -1));
    }
  }
}

module.exports = Square;
