$(document).ready(function(){
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
  const movies = data.results;
  movies.forEach(fucntion(movie){
   $('#list_movies').append('<li>' + movie.title + '<li>');
  });
 });
});
