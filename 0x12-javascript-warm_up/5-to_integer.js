#!/usr/bin/node

const argument1 = process.argv[2];

if (typeof argument1 !== 'number') {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argument1));
}
