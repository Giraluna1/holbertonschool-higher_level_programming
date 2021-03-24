#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let counter = 0;
    for (element of list) {
        if (element === searchElement) {
            counter += 1;
        }
    }
    return counter;
}
