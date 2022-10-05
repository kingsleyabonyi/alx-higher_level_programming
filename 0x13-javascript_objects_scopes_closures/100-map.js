#!/usr/bin/node

const arr = require('./100-data').list;
console.log(arr);
const newList = arr.map((x, index) => x * index);
console.log(newList);
