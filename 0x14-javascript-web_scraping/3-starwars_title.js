#!/usr/bin/node
/** a script to query an api and print it result */

const { error } = require('console');
const request = require('request');
const { json } = require('stream/consumers');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, res, data) => {
  if (!err && res.statusCode === 200) {
    const jsonBody = JSON.parse(data);
    console.log(jsonBody.title);
  }
});
