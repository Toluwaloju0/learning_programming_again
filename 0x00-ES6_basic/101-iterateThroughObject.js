export default function iterateThroughObject(reportWithIterator) {
  let str = "";
  for (const [ind, name] of reportWithIterator.entries()) {
    str += name;
    if (ind != reportWithIterator.length - 1) { str += " | "; }
  }
  return str
}
