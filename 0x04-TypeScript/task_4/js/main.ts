/// <reference path="./subjects/Teacher.ts"/> ///

// namespace Students {};

const cpp = new Students.Cpp();

cpp.setTeacher = {
    firstName: "Tolu",
    lastName: "Kayode",
    experienceTeachingC: 23,
};

console.log(cpp.getAvailableTeacher());