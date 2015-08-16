$(document).ready(function(){  
	$(document).on('click',"a[name='volver']",function() {  
		var id = $(this).attr('id');
    	var p = $('#proy').val();
    	var us_id = id.substr(1);
        $("#volverestado").dialog(
        		{
        			autoOpen: false,
        			title: 'Cambiar Actividad',
    				show: {
    					effect: "blind",
    					duration: 1000
    					},
    				hide: {
    					effect: "blind",
    					duration: 1000
    				},
    				width: 700,
    				height: 190,
    				position: {at: 'top'},
    				buttons: [
    				{
    					text: "Cambiar",
    					click: function() 
    					{
    						var sel = $('#seleacti').val();
    						$.ajax({
    							url: "/volver_actividad/",
    							data: {acti_id:sel,us:us_id},
    							type: 'POST',
    							success: function(result) 
    							{
    								
    								var a = JSON.parse(result);
    								
    								if(a.cambiar == 'no')
    									{
    									alert(a.mensaje);
    									return;
    									}
    								var newtr = "<tr><td id="+us_id+">"+a.ut+ " <a id=c"+us_id+" name='cambiar'><i class= fi-arrow-right></i></a></td><td></td><td></td></tr>";
    								$("td#"+us_id).parent().detach();
				      				$("table#"+a.actividad+" tr:last").after(newtr);
				      				 $("#volverestado").dialog( "close" );
				      				
    								
				        		
    							},
    							error: function(data) {
    				        	
    								alert('Error');
    							}
    						});
						}
				},
				{
					text: "Cancelar",
					click: function() {
						$( this ).dialog( "close" );
						}
				}
    			       ]
        			
        		});
    	$("#volverestado").dialog('open');
    	});   
    }); 