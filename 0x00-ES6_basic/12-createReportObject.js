export default function createReportObject(employeesList) {
  return {
    allEmployees: {...employeesList},
    getNumberOfDepartments() {
      let count = 0;
      for (const item in this.allEmployees) { count++; }
      return count;
    }
  }
}