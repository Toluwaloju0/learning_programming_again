;
var student1 = {
    firstName: "Toluwaloju",
    lastName: "Kayode",
    age: 10,
    location: "Home at Jushi",
};
var student2 = {
    firstName: "Jahjuwon",
    lastName: "Olorunfemi",
    age: 20,
    location: "Home at angwan godo",
};
var studentArray = [student1, student2];
// add a table to the document being processed
var table = document.createElement("table");
table.style.border = '2px red solid';
var tableBody = document.createElement("tbody");
studentArray.forEach(function (elem) {
    var tableRow = document.createElement("tr");
    var firstName = document.createElement("th");
    var location = document.createElement("td");
    firstName.textContent = "".concat(elem.firstName);
    location.textContent = "".concat(elem.location);
    tableRow.append(firstName, location);
    tableBody.appendChild(tableRow);
});
var caption = document.createElement("caption");
var tableHead = document.createElement("thead");
tableHead.innerHTML = "<tr><th>first name</th><th>location</th></tr>";
caption.textContent = "The table data";
table.append(caption, tableHead, tableBody);
document.body.appendChild(table);
