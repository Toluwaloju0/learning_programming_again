#!/usr/bin/node
// a script to print the factorial of a number

let num = Number(process.argv[2]);
let sum = 1;

if (Number.isNaN(num) || num <= 1) { console.log(1); } else {
  while (num > 0) {
    sum = sum * num--;
  }
  console.log(sum);
}
