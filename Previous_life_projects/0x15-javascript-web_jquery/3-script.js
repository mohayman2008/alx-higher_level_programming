// jQuery script add the class 'red' to <header> element
// when the user clicks on the tag DIV#red_header.

const $ = window.$;

$('DIV#red_header').click(() => { $('header').addClass('red'); });
