$('.dropdown-toggle').click(function (e) {
    if ($(document).width() > 768) {
        e.preventDefault();
        var url = $(this).attr('href');
        if (url !== '#') {
            window.location.href = url;
        }
    }
});

$(document).ready(function () {
    //Set the carousel options
    $('#quote-carousel').carousel({
        pause: true,
        interval: 4000,
    });
});

(function ($) {
    'use strict';
    jQuery(document).on('ready', function () {
        $('a.page-scroll').on('click', function (e) {
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top - 50
            }, 1500);
            e.preventDefault();
        });
    });
})(jQuery);