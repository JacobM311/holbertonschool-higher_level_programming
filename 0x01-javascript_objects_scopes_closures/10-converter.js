#!/usr/bin/node
'converts from base 10 to another base that gets passed';

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
