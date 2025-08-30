#!/usr/bin/node
/** a script to query an api */

const request = require('request');

request(process.argv[2], (err, res, data) => {
  if (!err && res.statusCode === 200) {
    jsonData = JSON.parse(data);
    let count = 0;  // a count for the name Wedge Antilles (character ID 18)
    // iterate over the parsed data and check if the characters in it have this id
    for (let a = 0; a < jsonData.count; a++) {
      const characters = jsonData.results[a].characters;
      for (let b = 0; b < characters.length; b++) {
        if (characters[b].slice(-4) === '/18/') { count++; }
      }
    }
    console.log(count);
  }
})