/// <reference path="Teacher.ts"/> ///

namespace Students{
    export class Subjects {
        teacher: Teacher

        set setTeacher(teacher: Teacher) {
            this.teacher = teacher;
        }
    }
}