#!/usr/bin/node
'prints x times “C is fun”';

const process = require('process');
const arg1 = process.argv[2];

if (arg1 === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; arg1 > i; i++) {
    console.log('C is fun');
  }
}
