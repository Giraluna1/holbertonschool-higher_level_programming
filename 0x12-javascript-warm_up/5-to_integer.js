#!/usr/bin/node

const argument1 = process.argv[2];

if (isNaN(argument1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argument1));
}
