// jQuery script fetches the character 'name' from
// +the URL: 'https://swapi-api.alx-tools.com/api/people/5/?format=json'

const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.getJSON(url).done((character) => { $('DIV#character').text(character.name); });
