#!/usr/bin/node
const argument = process.argv[2] * 1;
function factorial (fac) {
  return ((isNaN(fac)) || (fac === 1) ? 1 : (fac * factorial(fac - 1)));
}
console.log(factorial(argument));
