export const weakMap = new WeakMap();

export function queryAPI(object) {
  let count = weakMap.get(object) || 0;
  if (count >= 5) { throw new Error('Endpoint load is high'); }
  weakMap.set(object, ++count);
}

// export default { weakMap, queryAPI}
