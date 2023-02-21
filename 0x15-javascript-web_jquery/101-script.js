// jQuery script adds, removes and clears 'LI' elements from a list when the user clicks relevent buttons
// The script works fine when it is imported from the <head> tag

const $ = window.$;

$(document).ready(main);

function main () {
  const mylist = $('UL.my_list');
  const item = '<li>Item</li>';

  $('DIV#add_item').click(() => { $(mylist).append(item); });
  $('DIV#remove_item').click(() => { $(mylist).children(':last-child').remove(); });
  $('DIV#clear_list').click(() => { $(mylist).children().remove(); });
}
