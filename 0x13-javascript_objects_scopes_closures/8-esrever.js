#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (let item = list.length - 1; item >= 0; item--) {
    newList.push(list[item]);
  }
  return newList;
};
