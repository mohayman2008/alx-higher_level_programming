// The script updates the text color of the <header> element to red (#FF0000),
// Using DOM API
// The script works fine when it is imported from the <head> tag

document.addEventListener('DOMContentLoaded', main);

function main () {
  document.querySelector('header').style.color = '#FF0000';
}
