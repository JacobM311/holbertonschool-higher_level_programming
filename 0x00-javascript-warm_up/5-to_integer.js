#!/usr/bin/node
'prints My number: <first argument converted in integer> if the first argument can be converted to an integer';

const process = require('process');

const input = process.argv[2];
const number = Number(input);

if (!isNaN(number)) {
  console.log(`My number: ${Math.floor(number)}`);
} else {
  console.log('Not a number');
}
