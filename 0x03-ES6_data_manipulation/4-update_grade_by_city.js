export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList.filter((item) => item.location === city).map((item) => {
    item.grade = 'N/A';
    newGrades.forEach((element) => {
      if (item.id === element.studentId) { item.grade = element.grade; }
    });
    return item;
  });
}
