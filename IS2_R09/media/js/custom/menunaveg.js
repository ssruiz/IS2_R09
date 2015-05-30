$(document).ready(function() 
{
					$('.enlaceh').hover(function() 
					{ //mouse in
						$(this).stop().animate({ paddingBottom: '5px' },400);
						
					}, function() { //mouse out
						$(this).stop().animate({ paddingBottom: 0 }, 400);  				
					});
					
					$('ul.left li').mouseover(function(event){
	      					$(this).addClass("active");
	      				});
	      			$('ul.left li').mouseleave(function(event){
	      					$(this).removeClass("active");
	      				});
	      			 
	      			$(function() {
	      				$( document ).tooltip();
	      				});

	      			
});
				