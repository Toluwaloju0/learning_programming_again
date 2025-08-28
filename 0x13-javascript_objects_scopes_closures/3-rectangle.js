#!/usr/bin/node
/**
 * a script to create a rectangle class
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // a method to print the rectangle

    let str = '';

    for (let a = 0; a < this.height; a++) {
      for (let b = 0; b < this.width; b++) { str += 'X'; }
      str += '\n';
    }
    console.log(str.slice(0, -1));
  }
}

module.exports = Rectangle;
