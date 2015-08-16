$(document).ready(function(){  
  
    	$(document).on('click',"a[name='sacarrelease']",function() {
    		
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
    	            	$('#prioridad').val(a.priori)
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
    					text: "Aprobar para Release",
    					click: function() {
    						$.ajax({
    							url: "/sacar_release/",
    			          		type: 'GET',
    			          		data: {k:i},
    			          		datatype: 'json',
    			          		contentType: "application/json; charset=utf-8",
    			          		success: function(result) {
    			          			
    			          			var a = jQuery.parseJSON(result);
    			          			if(a.lanzar == 'no'){
    			          				alert(a.mensaje);
    			          			}
    			          			else{
    			          				alert('User Story aprobado para release');
    			          				$("td#"+i).parent().detach();
    			          				var newtr = "<li>"+a.us+" - <a title='Ver Información' id=r"+i+" name='Releaseinfo' <i class='fi-page'></i></a></li>";
    			          				$("ul#listaRelease").append(newtr);
    			          			}
    			          			
    			          		},
    			          		error: function(){
    			          			alert('error');
    			          		}
    						});
    						$( this ).dialog( "close" );
    						}
    				},
    				
    				{
    					text: "Cancelar",
    					click: function() {
    						$( this ).dialog( "close" );}
    				},
    				
    							]
    			});
    	       $("#inforus").dialog('open');
            },
            error: function() {
                alert('Error occured');
            }		
        		});
    		
    		});
    	
});
