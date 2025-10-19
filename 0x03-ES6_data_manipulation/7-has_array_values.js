export default function hasValuesFromArray(mySet, myArr) {
  for (const elem of myArr) {
    if (!mySet.has(elem)) { return false; }
  }
  return true;
}
