// jQuery script fetches from 'https://fourtonfish.com/hellosalut/?lang=fr'
// +and displays the value of 'hello' from that fetch in the HTML tag 'DIV#hello'
// The script works fine when it is imported from the <head> tag

const $ = window.$;
// const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
// ## The API URL has been changed ##
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(main);

function main () {
  $.ajax({
    url: url
  }).done((data) => {
    $('DIV#hello').text(data.hello);
  });
}
