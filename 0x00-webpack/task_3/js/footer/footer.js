const $ = require('jquery');
require('./footer.css');

$(document).ready(() => {
  const footer = $('<footer></footer>');
  footer.append('<p>Copyright - Holberton School</p>');
  $('body').append(footer);

  console.log('Init footer');
});
