$(document).ready(function () {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
      $.each(data.results, function (index, movie) {
        const listItem = $('<li></li>').text(movie.title);
        $('#list_movies').append(listItem);
      });
    });
  });