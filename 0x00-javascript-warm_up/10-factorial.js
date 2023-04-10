#!/usr/bin/node
'computes and prints a factorial';

const process = require('process');

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const input = parseInt(process.argv[2], 10);
const result = factorial(input);

console.log(result);
