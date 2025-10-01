export default function createIteratorObject(report) {
  const employees = []
  for (const item in report.allEmployees) {
    employees.push(...report.allEmployees[item])
  }
  return employees;
}
