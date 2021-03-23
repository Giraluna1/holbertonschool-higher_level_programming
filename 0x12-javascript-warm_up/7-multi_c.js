#!/usr/bin/node

const argument = process.argv[2];

if (isNaN(argument)) {
  console.log('Missing number of occurrences');
} else {
  for (let item = 0; item < argument; item++) {
    console.log('C is fun');
  }
}
