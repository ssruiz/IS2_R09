$(document).ready(function(){  
	$('#selfluj').click(function() {  
    	var sel = $('#selef').val();
    	var p = $('#proy').val()
        $.ajax({
        	url: "/ust_load/",
        	data: {fluj_id:sel,p:p},
        	type: 'GET',
        	dataType: 'html',
        	success: function(datos) {
        		$('#formu').append(datos).html();
        		$('#btn').hide('slide','slow');
        		var alt = $('#alta').val();
        		var med = $('#media').val();
        		var baj = $('#baja').val();
        		botonSegunPrio(alt,med,baj);
        	}
        });
    	});   
    });  