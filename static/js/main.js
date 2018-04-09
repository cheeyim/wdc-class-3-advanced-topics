$(document).ready(function() {
  $('.js-favorite-coin').on('click', function(evt){
    evt.preventDefault();
    var $elem = $(this);
    var $icon = $elem.find('i.fa')
    console.log($elem.data('coin-id'))

    $.post(window.APP_CONF.favorite_url, {
      coinId: $(this).data('coin-id'),
      csrfmiddlewaretoken: window.APP_CONF.csrf_token
    }, function(content, success){
      if(!success){
        console.log(data)
        return;
      }
      $icon.toggleClass('fa-star')
      $icon.toggleClass('fa-star-o')
    });
  });
});
