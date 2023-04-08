#!/usr/bin/node
'prints two arguments passed to it';

const process = require('process');

const arg1 = process.argv[2] !== undefined ? process.argv[2] : 'undefined';
const arg2 = process.argv[3] !== undefined ? process.argv[3] : 'undefined';

console.log(`${arg1} is ${arg2}`);
