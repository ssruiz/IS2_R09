$(document).ready(function(){
	$('#selef').change(function(){
		if(!$("#btn").is(':visible')){
			$('#btn').toggle('slide','slow');
			$('#formu').detach();
			$('releases').detach();
		}
	});
	
});