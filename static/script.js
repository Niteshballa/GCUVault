

function details(movieid)
{
  var vid;
$.get("https://api.themoviedb.org/3/movie/"+movieid+"?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=1",
function showmovie(result)
{
$.get("https://api.themoviedb.org/3/movie/"+movieid+"/videos?api_key=9824d5d7ab77a02aa6e9cc1b18bab686&language=en-US",
function(x){vid = x.results[0].key;
 //console.log(result);
 $('#ta').html("")
 $('#un').html("")
 $('#up').html("")
 $('#lp').html("")
 $('#ln').html("")
 $('#n17').html("")
 $("#thy").html("")
 $('#lns').html("")

 $('#animepopular').html("")

 $('#displaysearchdata').html("")
 $('#mvepopular').html("");
 $('#main').html("")
 $('#toprated').html("")
 $('html,body').scrollTop(0);
  $('#displayresult').append(

    				'<div class="container">'+
            '<div class="section-title"><a href="index.html">Go back to home</a></div>'+
            '<div class="section-title"><br>Trailer:</div>'+
    					'<div class="page">'+
    						'<div class="content">'+
                '<section class="trailer">'+
    '<div class="trailer_frame">'+
    '	<iframe width=100% height=100% src="https://www.youtube.com/embed/'+vid+'" frameborder="0" allowfullscreen></iframe>'+

                '</div></div>'+
                '<div>'+
                    '<h2 class="section-title">'+result.title+'</h2>'+
                    '<div class="movie-summary">'+
                        '<ul class="movie-meta">'+
                        '<li><strong>Original title : </strong>'+result.original_title+'</li>'+
                        '<li><strong>Year : </strong>( '+result.release_date.substring(0,4)+')</li>'+
                        '<li><strong>Tag line : </strong>'+result.tagline+'</li>'+
                        '<li><strong>Plot : </strong><br>'+result.overview+'</li>'+
                        '<li><strong>Rating : </strong>'+result.vote_average*10+'%</li>'+
                        '<li><strong>Length : </strong>'+result.runtime+'mins</li>'+
                        '<li><strong>Category : </strong>'+ result.genres[0].name+', '+result.genres[1].name+'</li>'+

                        '</ul>'+'</div>'+

                        '</div>'+'</div>'+'</div>');
});
});
}








function webseries(wbsid)
{
$.get("https://api.themoviedb.org/3/tv/"+wbsid+"?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=1",
function showwebseries(result)
{

  $('#un').html("")
  $('#up').html("")
  $('#lp').html("")
  $('#ln').html("")
  $("#thy").html("")
  $('#lns').html("")
  $('#ws').html("")
  $('#animepopular').html("")

  $('#wbspopular').html("")
  $('#mvepopular').html("")
 $('#topratedwbs').html("")
 $('#toprated').html("")
 $('#displaysearchdata').html("")
 $('#main').html("");
$('html,body').scrollTop(0);
  //console.log(result);
  $('#displayresult').append(
    				'<div class="container">'+
    					'<div class="page">'+
              '<div class="content">'+
    '<div class="row">'+
    '<div class="col-md-6">'+
    '<figure class="movie-poster"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+result.poster_path+'" alt="webseries"></figure>'+

                '</div>'+
                '<div class="col-md-7">'+
                    '<h2 class="section-title">'+result.name+'</h2>'+
                    '<div class="movie-summary">'+
                        '<ul class="movie-meta">'+
                        '<li><strong>Total Seasons : </strong>'+result.number_of_seasons+'</li>'+
                        '<li><strong>Latest Season : </strong> Season '+result.number_of_seasons+'</li>'+
                        '<li><strong>Episode run time : </strong> '+result.episode_run_time+'mins</li>'+
                        '<li><strong>Originl name : </strong>'+result.original_name+'</li>'+
                        '<li><strong>Plot : </strong><br>'+result.overview+'</li></ul>'+
                    '</div>'+
                    '<ul class="movie-meta">'+
                        '<li><strong>Rating : </strong>'+result.vote_average*10+'%</li>'+
                          '<li><strong>Category : </strong>'+ result.genres[0].name+'</li>'+
                        '<li><div class=innermeter></div></li>'+
                    '</ul>'+
                    '</ul>'+'</div>'+'</div>'+'</div>'+'</div>'+'</div>'+'</div>'+'</div>');
});
}


var wbsid;





function searchitems(x,i)
{
  //console.log(x.results[i]);
  $('#displaysearchdata').append('<div class="movie"><figure class="movie-poster"><a onclick="details('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="search movies"></a></figure>'+
      '<div class="movie-title"><a onclick="details('+x.results[i].id+')">'+x.results[i].title+'</a></div></div>');
}




function wbspopularitems(x,i)
{
  //console.log(x.results[i]);
  $('#wbspopular').append('<div class="movie"><figure class="movie-poster"><a onclick="webseries('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="popular webseries"></a></figure>'+
      '<div class="movie-title"><a onclick="webseries('+x.results[i].id+')">'+x.results[i].name+'</a></div></div>');
}

function animepopularitems(x,i)
{
  //console.log(x.results[i]);
  $('#animepopular').append('<div class="movie"><figure class="movie-poster"><a onclick="webseries('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="popular anime"></a></figure>'+
      '<div class="movie-title"><a onclick="webseries('+x.results[i].id+')">'+x.results[i].name+'</a></div></div>');
}

function top10holly(x,i)
{
  //console.log(x.results[i]);
  $('#top10holly').append('<div class="movie"><figure class="movie-poster"><a onclick="details('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="top rated"></a></figure>'+
      '<div class="movie-title"><a onclick="details('+x.results[i].id+')">'+x.results[i].title+'</a></div></div>');
}

function toprateditems(x,i)
{
  //console.log(x.results[i]);
  $('#toprated').append('<div class="movie"><figure class="movie-poster"><a onclick="details('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="top rated"></a></figure>'+
      '<div class="movie-title"><a onclick="details('+x.results[i].id+')">'+x.results[i].title+'</a></div></div>');
}

function toprateditems2(x,i)
{
  //console.log(x.results[i]);
  $('#toprated2').append('<div class="movie"><figure class="movie-poster"><a onclick="details('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="top rated movies 2"></a></figure>'+
      '<div class="movie-title"><a onclick="details('+x.results[i].id+')">'+x.results[i].title+'</a></div></div>');
}

function toprateditems3(x,i)
{
  //console.log(x.results[i]);
  $('#toprated3').append('<div class="movie"><figure class="movie-poster"><a onclick="details('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="top rated movies 3"></a></figure>'+
      '<div class="movie-title"><a onclick="details('+x.results[i].id+')">'+x.results[i].title+'</a></div></div>');
}

function toprateditems4(x,i)
{
  //console.log(x.results[i]);
  $('#toprated4').append('<div class="movie"><figure class="movie-poster"><a onclick="details('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="top rated movies 4"></a></figure>'+
      '<div class="movie-title"><a onclick="details('+x.results[i].id+')">'+x.results[i].title+'</a></div></div>');
}

function toprateditems5(x,i)
{
  //console.log(x.results[i]);
  $('#toprated5').append('<div class="movie"><figure class="movie-poster"><a onclick="details('+x.results[i].id+')"><img src="https://image.tmdb.org/t/p/w185_and_h278_bestv2/'+x.results[i].poster_path+'" alt="top rated movie 5"></a></figure>'+
      '<div class="movie-title"><a onclick="details('+x.results[i].id+')">'+x.results[i].title+'</a></div></div>');
}




var movieid;









//top_rated

$.get("https://api.themoviedb.org/3/movie/top_rated?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=1",
       function popular(toprated){
           // console.log(popularData);
           toprated.results.forEach(function(x,i){toprateditems(toprated,i);});
       });

       $.get("https://api.themoviedb.org/3/movie/top_rated?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=2",
              function popular(toprated){
                  // console.log(popularData);
                  toprated.results.forEach(function(x,i){toprateditems2(toprated,i);});
              });

              $.get("https://api.themoviedb.org/3/movie/top_rated?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=3",
                     function popular(toprated){
                         // console.log(popularData);
                         toprated.results.forEach(function(x,i){toprateditems3(toprated,i);});
                     });

                     $.get("https://api.themoviedb.org/3/movie/top_rated?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=4",
                            function popular(toprated){
                                // console.log(popularData);
                                toprated.results.forEach(function(x,i){toprateditems4(toprated,i);});
                            });

                            $.get("https://api.themoviedb.org/3/movie/top_rated?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=5",
                                   function popular(toprated){
                                       // console.log(popularData);
                                       toprated.results.forEach(function(x,i){toprateditems5(toprated,i);});
                                   });
//moviesuggestions


//$.get("https://api.themoviedb.org/3/movie/top_rated?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=2",
    //   function popular(popularData){
           // console.log(popularData);
    //       popularData.results.forEach(function(x,i){mvesgstitems(popularData,i);});
    //   });








       $.get("https://api.themoviedb.org/3/tv/popular?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=1",
      function wbspop(srs){
          //console.log(srs);
                    srs.results.forEach(function(x,i){wbspopularitems(srs,i);});
            });
            $.get("https://api.themoviedb.org/3/tv/top_rated?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&page=1",
           function animepop(aps){
            // console.log(srs);
                         aps.results.forEach(function(x,i){animepopularitems(aps,i);});
                 });







$('#searchIcon').click(function () {
        console.log($('#searchBox').val());
        if($('#searchBox').val()!== "") {
            $.get('https://api.themoviedb.org/3/search/movie?api_key=c7bcfaf589024c0a81002dd112a1d6c5&language=en-US&query='+$('#searchBox').val()+'&page=1&include_adult=false',
            function search(searchData){
            // console.log(searchData);
            // console.log($('#searchBox').val());
                $('#displayresult').html("");
                $('#main').html("");
                $('#displaysearchdata').html("");
                console.log(searchData)
                searchData.results.forEach(function(x,i){searchitems(searchData,i)})});
        }
    });
