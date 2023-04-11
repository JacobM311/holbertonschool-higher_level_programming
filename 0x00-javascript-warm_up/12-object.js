#!/usr/bin/node
'changes value from 12 to 89 literally right after we define it';

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.value = 89;

console.log(myObject);
