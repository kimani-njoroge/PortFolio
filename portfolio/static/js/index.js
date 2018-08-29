/**
 * Created by sam on 29/08/18.
 */
$(window).scroll(function(){
	$('nav').toggleClass('scrolled', $(this).scrollTop() > 100);
});