$(document).ready(function(){
$('#toggle_header').click(function(){
  if ($('header').hasClass('red')){
   $('header').removeClass('red').addCLass('green'); 
  }else{
    $('header').reomveClass('green').adClass('red');
  }
});
});
