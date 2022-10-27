$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    $.each(data.results, function (index, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
