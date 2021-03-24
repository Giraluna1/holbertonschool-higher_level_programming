#!/usr/bin/node

const sorted = new Float64Array(process.argv.slice(2)).sort();

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(sorted[sorted.length - 2]);
}
