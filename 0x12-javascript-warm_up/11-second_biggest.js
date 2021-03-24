#!/usr/bin/node

const sorted = new Float64Array(process.argv.slice(2).sort());

if (process.argv.length < 4) {
  console.log(0);
} else {
  const secondBigest = Number(sorted[sorted.length - 2]);
  console.log(secondBigest);
}
