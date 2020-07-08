$( document ).ready(function() {



// $(".bad_value").html("1");



jQuery.get('192.168.178.41:8123/lovelace/1', function(data) {
    console.log(data);
});


});


