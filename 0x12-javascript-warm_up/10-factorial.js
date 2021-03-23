#!/usr/bin/node

const firstInt = parseInt(process.argv[2]);

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(firstInt));
