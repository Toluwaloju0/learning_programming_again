interface Student {
    firstName: string,
    lastName: string,
    age: number,
    location: string
};

const student1: Student = {
    firstName: "Toluwaloju",
    lastName: "Kayode",
    age: 10,
    location: "Home at Jushi",
};

const student2: Student = {
    firstName: "Jahjuwon",
    lastName: "Olorunfemi",
    age: 20,
    location: "Home at angwan godo",
};

const studentArray: Student[] = [student1, student2];

// add a table to the document being processed
const table = document.createElement("table");
table.style.border = '2px red solid';
const tableBody = document.createElement("tbody");

studentArray.forEach(elem => {
    const tableRow = document.createElement("tr");
    const firstName = document.createElement("th");
    const location = document.createElement("td");
    firstName.textContent = `${elem.firstName}`;
    location.textContent = `${elem.location}`;
    tableRow.append(firstName, location);
    tableBody.appendChild(tableRow)
});

const caption = document.createElement("caption");
const tableHead = document.createElement("thead");
tableHead.innerHTML = "<tr><th>first name</th><th>location</th></tr>";
caption.textContent = "The table data";
table.append(caption, tableHead, tableBody);
document.body.appendChild(table);
