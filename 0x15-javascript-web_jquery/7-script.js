$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    $('DIV#character').text(data.name);
  }
});
