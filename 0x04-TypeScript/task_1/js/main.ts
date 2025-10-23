interface Teacher {
    readonly firstName: string;
    readonly lastName: string;
    fullTimeEmployee: boolean;
    yearsOfExperience?: boolean;
    [key: string]: boolean | string | number;
};

interface Director extends Teacher {
    numberOfReports: number;
};

function printTeacher(firstName:string, lastName: string) { return `${firstName[0]}. ${lastName}`; }

interface printTeacherFunction {
    (firstName: string, lastName: string): string;
}

interface Student {
    firstname: string;
    lastName: string;
}

interface studentConstructor {
    (firstName: string, lastName: string): void;
}

class StudentClass {
    firstName: string;
    lastName: string;

    constructor(firstName: string, lastName:string) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    workOnHomework() { return "Currently working"; }

    displayName() { return this.firstName; }
}
