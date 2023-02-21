// jQuery script fetches and prints how to say “Hello” depending on the language
// The script works fine when it is imported from the <head> tag

const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=';

$(document).ready(main);

function main () {
  function getHello () {
    $.ajax({
      url: url + $('INPUT#language_code').val()
    }).done((data) => { $('DIV#hello').text(data.hello); });
  }

  $('INPUT#btn_translate').click(getHello);
}
