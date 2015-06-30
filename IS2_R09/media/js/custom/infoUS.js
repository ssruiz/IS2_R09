$(document).ready(function(){  
  
    	$(document).on('click',"a[name='cambiar']",function() {
    		
    		var id = $(this).attr('id')
    		var activ = $(this).closest('table').attr('id');
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
    	            			        	  text: "Agregar Comentario",
    	            			        	  click: function() {
    	            			        		  $("#comentario").dialog(
    	            			        				  {
    	            			        					  autoOpen: false,
    	            			        					  modal: true,
    	            			        					  dialogClass: "table",
    	            			        					  title: 'Agregar Comentario',
    	            			        					  width: 900,
    	            			        					  buttons: [
    			    				{
    			    					text: "Guardar",
    			    					icons: {primary:'fi-trash'},
    			    					click: function() {
    			    						$.ajax({
    			    							url: "/crear_comentario_us/",
    			    							type: "POST",
    			    							data: {k:i,nombre:$('#nombrecom').val(),ht:$('#horastrab').val(),c:$('#coment').val()},
    			    							success: function(result) {
    			    				      			var r = jQuery.parseJSON(result);
    			    				      			alert(r.mensaje);
    			    				      			$('#ttrabajado').val(r.ht);
    			    				      			 $("#comentario").dialog( "close" );
    			    				      		},
    			    				      		error : function(){
    			    				      			alert('errorrrrrrr');
    			    				      		}
    			    						});
    			    						}
    			    				},
    			    				
    			    				{
    			    					text: "Cancelar",
    			    					click: function() {
    			    						$( this ).dialog( "close" );}
    			    				},
    			    				
    			    							]
    			    			});
    	            			        		  $("#comentario").dialog('open');
    					}
    				},
    				
    				{
    					text: "Cambiar Estado",
    					click: function() {
    						
    				    	
    						$.ajax({
    				      		url: "/cambiar_estado/",
    				      		type: 'GET',
    				      		data: {k:i},
    				      		datatype: 'json',
    				      		
    				      		contentType: "application/json; charset=utf-8",
    				      		success: function(result) {
    				      			
    				      			var a = jQuery.parseJSON(result);
    				      			if(a.cambiar == 'no'){
    				      				alert(a.mensaje);
    				      				return;
    				      			}
    				      			if(a.estado == 'dg'){
    				      				var newtr = "<tr><td></td><td id="+i+"><a id=v"+i+" name='volver'><i class= fi-arrow-left></i></a> "+ a.ut+ " <a id=c"+i+" name='cambiar'><i class= fi-arrow-right></i></a></td><td></td></tr>"
        				      			$("td#"+i).parent().replaceWith(newtr);
    				      				
    				      			}
    				      			else if(a.estado == 'de'){
    				      				var newtr = "<tr><td></td><td></td><td id="+i+"><a id=v"+i+" name='volver'><i class= fi-arrow-left></i></a> "+ a.ut+ " <a id=c"+i+" name='cambiar'><i class= fi-arrow-right></i></a></td></tr>"
        				      			$("td#"+i).parent().replaceWith(newtr);
    			
    				      			}
    				      			else{
    				      				var newtr = "<tr><td id="+i+"><a id=v"+i+" name='volver'><i class= fi-arrow-left></i></a> "+ a.ut+ " <a id=c"+i+" name='cambiar'><i class= fi-arrow-right></i></a></td><td></td><td></td></tr>"
    				      				$("td#"+i).parent().detach();
    				      				$("table#"+a.actividad+" tr:last").after(newtr);
    				      			}
    				      			
    				      		
    				      		 
    				      			
    				            
    				        },
    				        
    				        error: function(data) {
    				        	
    				            alert();
    				        }
    				      	});
    						
    					
    					}
    				},
    				
    				{
    					text: "A Release",
    					click: function() {
    						$( this ).dialog( "close" );}
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