#!/usr/bin/node
/* a script to execute a function */

export function callMeMoby (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
}
