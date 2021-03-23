#!/usr/bin/node

const argument = parseInt(process.argv[2]);

if (isNaN(argument)) {
  console.log('Missing size');
} else {
  for (let item = 0; item < argument; item++) {
    console.log('X'.repeat(argument));
  }
}
