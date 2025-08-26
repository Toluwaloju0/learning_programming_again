#!/usr/bin/node
// a script to print a sentence for a specifies number of times

let num = Number(process.argv[2]);

if (Number.isNaN(num)) { console.log('Missing number of occurrences'); } else {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
