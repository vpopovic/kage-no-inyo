setInterval(function(){
    pk = $('.active-entry').data('pk');
    $('.active-entry .badge').load('/ajax/' + pk);
}, 60000);
