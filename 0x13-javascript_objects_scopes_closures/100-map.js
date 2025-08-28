#!/usr/bin/node

const list = require('./100-path').list;

const newList = list.map((element, index) => {
  return element * index;
});

console.log(list, '\n', newList);
