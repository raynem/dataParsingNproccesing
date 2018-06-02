/**
 * Created by HP on 09.05.2018.
 */
$(document).ready(function() {
$.ajax({
	    type: "GET",
	    url: '/load_ajax',
	    success: function(result){
	        for(i = 0; i < result.length; i++){
            $('#theme').append($('<option>', {
    value: result[i] ,
    text: result[i]
    }));}
	    }});

    $("#test-circle").circliful({
                animationStep: 5,
                foregroundBorderWidth: 5,
                backgroundBorderWidth: 15,
                percent: 75
           });
});


function load_autors () {
    topic = $('#theme').val();
    if (topic == "Choose topic"){
        $(".tbl").hide();
        return;
    }
    $.ajax({
	    type: "GET",
	    url: '/load_autors',
        data: { 'val' : topic },
	    success: function(result){
	        $('.table > tbody:last-child').text('');
	        var mySelect = document.getElementById('author');
            mySelect.options.length = 0;
             $('#author').append($('<option>', {
                value: '',
                text: 'Choose author'
                }));
             i=1;
	        for(key in result){
            $('#author').append($('<option>', {
    value: key ,
    text: key
    }));
	       $('.table > tbody:last-child').append('<tr><td>'+ i.toString() +'</td><td>'+ key +'</td><td>'+result[key]+'</td></tr>');
	        i++;
	        }
	        $(".tbl").show()

	    }});}

function showCircle () {
    $("#test-circle").empty();
    $("#test-circle").show();
      $.ajax({
	    type: "GET",
	    url: '/load_percent',
        data: { 'author' : $('#author').val(),
                'topic' : $('#theme').val()},
	    success: function(result) {
            $("#test-circle").circliful({
                animationStep: 5,
                foregroundBorderWidth: 5,
                backgroundBorderWidth: 15,
                percent: result
           });
        }});




}