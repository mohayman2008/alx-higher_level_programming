// jQuery script fetches and lists the 'title' for all movies,
// +by using this URL: 'https://swapi-api.alx-tools.com/api/films/?format=json'

const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.getJSON(url).done((result) => {
  const movies = result.results;
  const ul = $('UL#list_movies');

  $(movies).each(function (idx, movie) {
    ul.append('<LI>' + movie.title + '</LI>');
  });
});
