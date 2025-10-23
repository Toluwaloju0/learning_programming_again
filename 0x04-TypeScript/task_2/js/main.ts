interface DirectorInterface {
    workFromHome(): string;
    getCoffeeBreak(): string;
    workDirectorTasks(): string; 
};

interface TeacherInterface {
    workFromHome(): string;
    getCoffeeBreak(): string;
    workTeacherTasks(): string;    
};

class Director {
    workFromHome(): string { return "Working from home"; }
    
    getCoffeBreak(): string { return "Getting a Coffee Break"; }

    workDirectorTasks(): string { return "Getting to Director Tasks"; }
}

class Teacher {
    workFromHome(): string { return "Cannot work from Home"; }

    getCoffeeBreak(): string { return "Cannot get Coffee Break"; }

    workTeacherTasks(): string { return "Getting to Work"; }
}

function createEmployee(salary: number | string): void | Teacher | Director {
    if (Number.isNaN(salary)) { return null; }
    let salaryNumber: number;
    if (typeof(salary) === "string") { salaryNumber = Number.parseInt(salary); } else {salaryNumber = salary; }
    if (salaryNumber < 500) { return new Teacher(); }
    return new Director();
}

function isDirector(employee: Teacher | Director): boolean {
    if (employee instanceof Director) { return true; }
    return false;
}

function executeWork(employee: Teacher | Director | any): void {
    if (isDirector(employee)) { console.log(employee.workDirectorTasks()); } else { console.log(employee.workTeacherTasks()); }
}

type Subjects = "Math" | "History";

function teachClass(todayClass: Subjects): void { console.log(`Teaching ${todayClass}`); }
