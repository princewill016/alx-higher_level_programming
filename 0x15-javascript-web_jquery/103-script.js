// Task 14 - Fetch hello translation with click or ENTER key using jQuery
$(function () {
  function fetchTranslation() {
    const langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);
  
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});
