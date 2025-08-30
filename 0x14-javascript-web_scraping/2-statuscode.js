#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
    if (err) { console.log(err); } else { console.log('Code: ' + res.statusCode); }
});