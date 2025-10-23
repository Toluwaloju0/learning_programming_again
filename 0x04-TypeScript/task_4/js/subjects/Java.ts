/// <reference path="Teacher.ts"/> ///

namespace Students {
    export interface Teacher {
        experienceTeachingJava?: number;
    };

    export class Java extends Subjects {
        constructor() { super(); }

        getRequirements() { return "Here is the list of requirements for teaching Java"; }

        getAvailableTeacher() {
            if (this.teacher.experienceTeachingJava === undefined) { return "No available teacher"; }
            return `Teacher name ${this.teacher.firstName}`;
        }
    }
};
