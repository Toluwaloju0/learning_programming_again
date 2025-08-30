#!/usr/bin/node
/** a script to query an api and store it result in a file */

const req = require('request');
const fs = require('fs');

req(process.argv[2], (err, res, data) => {
  if (!err && res.statusCode === 200) {
    fs.writeFile(process.argv[3], data, (err) => {
      if (err) { console.log(err); }
    });
  }
});