/// <reference path="Teacher.ts"/> ///

namespace Students {
    export interface Teacher {
        experienceTeachingC?: number;
    };

    export class Cpp extends Subjects {
        constructor() { super(); }
        getRequirements(): string { return "Here is the list of requirements for Cpp"; }

        getAvailableTeacher(): string {
            if (this.teacher.experienceTeachingC === undefined) {return "No available teacher"; }
            return `Available Teacher ${this.teacher.firstName}`;
        }
    };
};