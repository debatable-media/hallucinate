$(window).scroll(function(){
	var st = $(this).scrollTop();
	var op = 0.2+0.8*(Math.min(Math.max(0.0, st-100.0), 200.0)/200.0);
	$('nav').css('background-color', 'rgba(0,0,0,' + op + ')');
});

$("#post-content").keyup(function (e) {
    autoheight(this);
});

function autoheight(a) {
    if (!$(a).prop('scrollTop')) {
        do {
            var b = $(a).prop('scrollHeight');
            var h = $(a).height();
            $(a).height(h - 5);
        }
        while (b && (b != $(a).prop('scrollHeight')));
    };
    $(a).height($(a).prop('scrollHeight') + 20);
}

autoheight($("#post-content"));

