const jquery = require('jquery');
const _ = require('lodash');

const link = document.createElement("link");
link.rel = "stylesheet";
link.href = "../css/main.css";
document.head.appendChild(link);


jquery('body').append('<p>Holberton Dashboard</p>');
jquery('body').append('<p>Dashboard data for the students</p>');
jquery('body').append('<button>Click here to get started</button>');
jquery('body').append('<p id=count></p>');
jquery('body').append('<p>Copyright - Holberton School</p>');

let count = 0;

function updateCounter() {
  jquery('button').on('click', () => {
    count++;
    jquery('p#count').text(`${count}`);
  });
}
  
_.debounce(updateCounter);
updateCounter();