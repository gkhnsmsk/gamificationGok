$( document ).ready(function() {



$.get('output.txt', function(data) {
    var obj = jQuery.parseJSON(data);

    console.log(obj[0]["bad"]);

    $(".bad_value").html(obj[0]["bad"]);
    $(".cool_value").html(obj[0]["cool"]);
    $(".good_value").html(obj[0]["good"]);
    $(".perfect_value").html(obj[0]["perfect"]);

    var width = (obj[0]["daily"] * 10) ;


    if (obj[0]["daily"] > 10){
        width = 100;
    }
    
    $(".meter span").css("width", width+"%");


 }, 'text');


});


