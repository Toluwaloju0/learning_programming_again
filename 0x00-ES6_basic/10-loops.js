export default function appendToEachArrayValue(array, appendString) {
  for (let [ind, item] of array.entries()) {
    array[ind] = appendString + item;
  }
  return array;
}
