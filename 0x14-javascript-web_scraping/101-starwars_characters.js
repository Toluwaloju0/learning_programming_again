#!/usr/bin/node
/** a script to print the query to an api */

const req = require('request');

req.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, res, data) => {
  if (!err && res.statusCode === 200) {
    const characters = JSON.parse(data).characters;
    // iterate over the characters and query and print each name
    for (const character of characters) {
      req(character, (err, res, data) => {
        if (!err && res.statusCode === 200) {
          console.log(JSON.parse(data).name);
        }
      })
    }
  }
})