#!/usr/bin/node

exports.esrever = function (list) {
  const newArr = list.map(list.pop, [...list]);
  return (newArr);
};
