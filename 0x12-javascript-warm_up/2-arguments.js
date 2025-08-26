#!/usr/bin/node
// a programm to to print if arguments are passed to the command line when executing the script

const process = require('process');

if (process.argv.length === 2) { console.log('No argument'); } else if (process.argv.length === 3) { console.log('Argument found'); } else { console.log('Argunemts found'); }
