export default function createInt8TypedArray(length, position, value) {
  if (position >= length) { throw new Error('Position outside range'); }

  const myArr = new ArrayBuffer(10);
  const view = new Int8Array(myArr);
  view[position] = value;

  return myArr;
}
