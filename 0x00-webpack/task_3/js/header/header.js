const $ = require('jquery');
const image = require('../../assets/holberton-logo.jpg');
require('./header.css');

$(document).ready(() => {
  const header = $('<header></header>');
  const logo = $('<div id="logo"></div>');

  logo.css({
    'background-image': `url(${image})`,
    'background-size': '200px 200px',
    'background-repeat': 'no-repeat',
  });

  header.append(logo);
  header.append('<h1>Holberton Dashboard</h1>');

  $('body').prepend(header);

  console.log('Init header');
});
