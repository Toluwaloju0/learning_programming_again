#!/usr/bin/node
// a script to add two integers toghether

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

if (Number.isNaN(a) || Number.isNaN(b)) { console.log('NaN'); } else { console.log(`${a + b}`); }
