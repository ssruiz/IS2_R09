$(document).ready(function(){  
	$(document).on('click',"input[id='selsprint']",function() {  
    	var sel = $('#selesprinte').val();
    	var p = $('#proyectosp').val()
    	$('#btn').hide('slide','slow');
        $.ajax({
        	url: "/bd_load/",
        	data: {sp_id:sel,p:p},
        	type: 'GET',
        	datatype: 'json',
      		
      		contentType: "application/json; charset=utf-8",
      		success: function(result) {
        		var a = jQuery.parseJSON(result);
        		var d1 = a.trabajado;
        		var d2 = a.estimado;
        		var data = [
        		            {
        		            	data: d1,lines: { show: true },points: { show: true },label:'Trabajado' 
        		            }, 
	                        {
        		            	data:d2,lines: { show: true },points: { show: true },label:'Esperado' 
        		            		}
        		           ]
        		var options = {
        				 axisLabels: {
        			            show: true
        			        },
        			        xaxes: [{
        			        	tickDecimals: 0,
        			        	min : 1,
        			            axisLabel: 'Dias',
        			        }],
        			        yaxes: [{
        			        	
        			            position: 'left',
        			            axisLabel: 'Trabajo Remanente - Horas',}]
        			        
        		};
        		$.plot("#placeholder", data,options);
        		
        	}
        });
    	});   
    });  