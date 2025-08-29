$.get('https://hellosalut.stefanbohacek.com/?lang=ja', (data) => {
  $(document).ready(() => {
    $('div#hello').text(data.hello);
  });
});
