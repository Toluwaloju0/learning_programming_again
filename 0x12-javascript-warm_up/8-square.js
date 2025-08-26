#!/usr/bin/node
// a script to print a square

const num = Number(process.argv[2]);
let myStr = '';

if (Number.isNaN(num)) { console.log('Missing size'); } else {
  for (let a = 0; a < num; a++) {
    for (let b = 0; b < num; b++) {
      myStr += 'X';
    }
    console.log(myStr);
    myStr = '';
  }
}
