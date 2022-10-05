#!/usr/bin/node

exports.converter = function (base) {
  function convertTo (number) {
    return number.toString(base);
  }
  return convertTo;
};
