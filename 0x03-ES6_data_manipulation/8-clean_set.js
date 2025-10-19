export default function cleanSet(mySet, startString) {
  if (startString.length === 0) { return ''; }
  let string = '';
  mySet.forEach((element) => {
    if (element.slice(0, startString.length) == startString) {
      string += `${element.slice(startString.length)}-`;
    }
  });
  return string.slice(0, -1);
}
