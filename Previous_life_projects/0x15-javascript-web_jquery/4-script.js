// jQuery script toggle' to <header> element class between 'red' and 'green'
// when the user clicks on the tag DIV#red_header.

const $ = window.$;

$('DIV#toggle_header').click(() => {
  const myHeader = $('header');

  if (myHeader.hasClass('red')) {
    myHeader.removeClass('red');
    myHeader.addClass('green');
  } else if (myHeader.hasClass('green')) {
    myHeader.removeClass('green');
    myHeader.addClass('red');
  }
});
