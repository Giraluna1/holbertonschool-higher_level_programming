#!/usr/bin/node

const firstInt = parseInt(process.argv[2]);

function factorial(num) {
  let answer=1;
  for (let item = 2; item <= num; item++) {
    answer = answer * item;
  return answer;
}
result = factorial(firstInt);
console.log(result);
