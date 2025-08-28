#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  /**
     * a function toreturn the number of occurrences of
     * searchElement in list
     */

  let occurrences = 0;
  list.forEach(element => {
    if (element === searchElement) { occurrences++; }
  });
  return occurrences;
};
