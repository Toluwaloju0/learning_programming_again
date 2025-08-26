#!/usr/bin/node
// a  function to print arguments passed to the command line

const process = require('process');

if (process.argv.length < 3) { console.log('No argument'); } else {
  for (let a = 2; a < process.argv.length; a++) {
    console.log(process.argv[a]);
  }
}
