
$("ul.nav li a").each(function() {
    var link = $(this).attr('href');
    var url = window.location.pathname;
    url == link ? $(this).parent().addClass("active") : $(this).parent().removeClass("active");
});
