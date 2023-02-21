// jQuery script fetches from 'https://fourtonfish.com/hellosalut/?lang=fr'
// +and displays the value of 'hello' from that fetch in the HTML tag 'DIV#hello'
// The script works fine when it is imported from the <head> tag

const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(document).ready(main);

function main () {
  $.getJSON(url).done((result) => {
    $('DIV#hello').text(result.hello);
  });
}
