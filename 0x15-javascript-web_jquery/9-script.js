document.addEventListener('DOMContentLoaded', function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
    if (status === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
