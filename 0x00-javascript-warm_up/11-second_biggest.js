#!/usr/bin/node
'returns second largest of an array';

const process = require('process');

function secondLargest (numbers) {
  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (const number of numbers) {
    if (number > largest) {
      secondLargest = largest;
      largest = number;
    } else if (number > secondLargest && number < largest) {
      secondLargest = number;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2).map((arg) => parseInt(arg, 10));
const result = args.length <= 1 ? 0 : secondLargest(args);

console.log(result);
