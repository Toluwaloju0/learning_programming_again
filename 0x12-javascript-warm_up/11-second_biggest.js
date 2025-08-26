#!/usr/bin/node
// a code to determine the second bigest in a number

if (process.argv.length < 4) { console.log('0'); } else {
  // create two intergers for the first and second command line values
  let first, second;
  if (process.argv[2] >= process.argv[3]) {
    first = Number(process.argv[2]);
    second = Number(process.argv[3]);
  } else {
    first = Number(process.argv[3]);
    second = Number(process.argv[2]);
  }
  for (let a = 4; a < process.argv.length; a++) {
    const num = Number(process.argv[a]);
    if (num > second && num < first) { second = num; } else if (num > first && num > second) {
      second = first;
      first = num;
    }
  }
  console.log(second);
}
