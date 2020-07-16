$( document ).ready(function() {



// $(".bad_value").html("1");


$.get('test.txt', function(data) {
    var obj = jQuery.parseJSON(data);

    console.log(obj[2].state);
    $(".bad_value").html(obj[2].state);

 }, 'text');


});


