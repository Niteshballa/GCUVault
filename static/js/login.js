$(function() {

 
	$('#body').on('click', function(event) {
		// compare the element clicked (event.target) with the
		// element that has the click attached (this)
		if (event.target !== this)
		{
		return;
		}
		
		window.location.href ="http://127.0.0.1:8000/home";
		
	  });
	$('#home').on('click',function(e){
		window.location.href ="http://127.0.0.1:8000/home";
	});
});
