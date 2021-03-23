#!/usr/bin/node

const firstInt = process.argv[2];
const secondInt = process.argv[3];

function add (a, b) {
  return (a + b);
}

console.log(add(firstInt, secondInt));
