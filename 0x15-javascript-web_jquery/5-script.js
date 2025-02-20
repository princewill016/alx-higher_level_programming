// Task 6 - Add list item on click using jQuery
$(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
