
prioridades = function(altas,medias,bajas,id){
   	if(altas == 0)
   	{
   		if(medias != 0)
   		{
   			$("input[name^='cambmedia']").attr('disabled',false);
   			alert('Ha realizado el ultimo User Story con prioridad alta. Activando los de prioridad media.')
   		}
   		else
   		{
   			alert('Ha realizado el ultimo User Story con prioridad alta y/o media. Activando los de prioridad baja.')
   			$("input[name^='cambbaja']").attr('disabled',false);
   		}
   	}
   	 return 0;
   }
   
   botonSegunPrio = function(altas,medias,bajas,id){
   		if(altas != 0)
   		{
   			$("input[name^='cambmedia']").attr('disabled',true);
   			$("input[name^='cambbaja']").attr('disabled',true);
   		}
   		else
   		{
   			if(media != 0)
   			{
   				$("input[name^='cambmedia']").attr('disabled',false);
   				$("input[name^='cambbaja']").attr('disabled',true);
   			}
   			else
   				$("input[name^='cambbaja']").attr('disabled',false);
   			
   		}
   		return 0;
   	
   }
   
   cambiarEstadoUS = function(id){
	   alert(id);
	   $('#'+id+'ta').each(function(index){
		  alert( $(this).text());
	   });
   }