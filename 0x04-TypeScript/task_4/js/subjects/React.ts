/// <reference path="Teacher.ts"/> ///

namespace Students {
    export interface Teacher {
        experienceTeachingReact?: number;
    };

    export class React extends Subjects {
        constructor() { super(); }
        getRequirements() { return "Here is the list requirements for teaching React"; }

        getAvailableTeacher() {
            if (this.teacher.experienceTeachingReact === undefined) { return "No available teacher"; }
            return `Teacher name ${this.teacher.firstName}`;
        }
    }
};
