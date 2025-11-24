const $ = require('jquery');
const _ = require('lodash');
require('./body.css');

$(document).ready(() => {
  const btn = $('<button>Click Me</button>');
  const counter = $('<p id="counter">Clicks: 0</p>');

  $('body').append(btn);
  $('body').append(counter);

  let count = 0;

  btn.on('click', _.debounce(() => {
    count++;
    $('#counter').text(`Clicks: ${count}`);
  }, 500));

  console.log('Init body');
});
