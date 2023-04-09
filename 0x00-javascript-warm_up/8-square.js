#!/usr/bin/env node
'script that prints a square';

const process = require('process');

const input = process.argv[2];
const size = parseInt(input, 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
