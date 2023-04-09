#!/usr/bin/node
'prints the addition of 2 integers';

const process = require('process');

if (process.argv.length >= 4) {
  const a = parseInt(process.argv[2], 10);
  const b = parseInt(process.argv[3], 10);

  function add (a, b) {
    return a + b;
  }

  const result = add(a, b);
  console.log(result);
} else {
  console.log('NaN');
}
