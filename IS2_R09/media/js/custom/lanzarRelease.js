$(document).ready(function(){  
  
    	$(document).on('click',"input[id='sacarR']",function() {
    		var proyecto = $('#proy').attr('value');
        	$("#Release").dialog(
        			{
        				autoOpen: false,
        				title: 'US listos para Release',
        				show: {
        					effect: "blind",
        					duration: 1000
        				},
        			hide: {
        				effect: "blind",
        				duration: 1000
        			},
        			width: 700,
        			height: 490,
        			position: {at: 'top'},
        			buttons: [
        			          {	
        			        	  text: "Lanzar Release",
        			        	  click: function() {
        			        		  
        			        		  $.ajax({
        			        			    url: "/lanzar_release/",
        			                		type: 'GET',
        			                		data: {k:proyecto},
        			                		datatype: 'json',
        			                		contentType: "application/json; charset=utf-8",
        			                		success: function(result) {
        			                				var a = jQuery.parseJSON(result);
        			                				alert(a.mensaje);
        			                		},
        			                		error: function(){
        			                			alert('Error ocurrido! Vuelva a intentarlo');
        			                		}
        			          	         
        			        		  });
        			        		  }
        			          },
        			          {
        			        	  text: "Cancelar",
        			        	  click: function() {
        			        		  $( this ).dialog( "close" );}
        			          }
        			          ]
        			});
    	       $("#Release").dialog('open');
              		
    		});
    	
$(document).on('click',"a[name='Releaseinfo']",function() {
    		
    		var id = $(this).attr('id')
    		var i = id.substr(1);
    		$.ajax({
    			url: "/infoust/",
          		type: 'GET',
          		data: {k:i},
          		datatype: 'json',
          		
          		contentType: "application/json; charset=utf-8",
          		success: function(result) {
          				var a = jQuery.parseJSON(result);
    	            	$('#nombreus').val(a.nombre);
    	            	$('#testimado').val(a.test);
    	            	$('#ttrabajado').val(a.tt);
    	            	$('#descrip').val(a.des);
    	            	$('#prioridad').val(a.priori);
    	            	$("#inforus").dialog(
    	            	{
    	            				autoOpen: false,
    	            				title: 'Info User Story',
    	            				show: {
    	            					effect: "blind",
    	            					duration: 1000
    	            				},
    	            			hide: {
    	            				effect: "blind",
    	            				duration: 1000
    	            			},
    	            			width: 700,
    	            			height: 490,
    	            			position: {at: 'top'},
    	            			buttons: [
    			    	
    				
    				
    				{
    					text: "Aceptar",
    					click: function() {
    						$( this ).dialog( "close" );}
    				},
    				
    							]
    			});
    	       $("#inforus").dialog('open');
            },
            error: function() {
                alert('Error ocurrido. Vuelva a intentar');
            }		
        		});
    		
    		});
});
