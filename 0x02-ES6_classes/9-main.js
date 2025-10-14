import listOfStudents from './9-hoisting.js';

console.log(listOfStudents);
const listPrinted = listOfStudents.map(
  (student) => student.fullStudentDesription,
);
console.log(listPrinted);
