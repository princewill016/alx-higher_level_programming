// Task 13 - Fetch and display hello in different languages using jQuery
$(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
