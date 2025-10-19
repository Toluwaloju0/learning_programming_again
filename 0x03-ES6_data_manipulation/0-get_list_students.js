export default function getListStudents() {
  /** a function to create an array */

  const createArray = (id, name, location) => ({ id, name, location });
  return [
    createArray(1, 'Guillamine', 'San Francisco'),
    createArray(2, 'James', 'Columbia'),
    createArray(5, 'Serena', 'San Francisco'),
  ];
}
