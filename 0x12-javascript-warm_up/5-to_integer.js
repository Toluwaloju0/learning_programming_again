#!/usr/bin/node
// a script to print a number passed to the command line

const num = Number(process.argv[2]);
if (Number.isNaN(num)) { console.log('Not a number'); } else { console.log(`My number: ${num}`); }
