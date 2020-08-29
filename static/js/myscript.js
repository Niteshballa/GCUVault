function loadData(event) {
  event.preventDefault();
  // only display favourite list if items are there
$(".view-fav").on("click", function() {
  if ($.trim($(".favourite").html()).length) {
    $(".favourite").fadeToggle();
    $(".bg").fadeToggle();
  }
});

  let search;
  // check if no input
  // set default search to jaws
  if (!$("input").val()) {
    search = "bond";
  } else {
    search = $("input").val();
    $("input").val("");
  }

  // api and end points
  // create search with user input
  const api = "&api_key=c7bcfaf589024c0a81002dd112a1d6c5";
  const endpoint = `https://api.themoviedb.org/3/search/movie?query=${search}${api}`;
  const poster = "https://image.tmdb.org/t/p/w600/";

  let gridHtml = "";
  let selectedHtml = "";

  $.getJSON(endpoint, function(data) {

    // show film details in pop up
    $("body").on("click", "li", function(e) {
      $(".view-fav").fadeToggle();
      $(".selectedFilm").fadeIn();
      $(".bg").fadeToggle();
      // get number of list item
      // match this the data returned in results
      // to be able to pull through same info
      let index = $("li").index(this);
      let selected = data.results[index];
      // creating film pop up layout and info
      gridHtml = `
 <i class="fa fa-times close" aria-hidden="true"></i>
        <div class="selectedFilm__img">
                <img class ="selectedFilm__poster" src ="${poster}${selected.poster_path}">
         </div>
         <div class="selectedFilm__content">
            <h2>${selected.title}</h2>
            <h3>Overview</h3>
            <p>${selected.overview}</p>

        <span class ='add-fav'>Add to favourites <i class="fa fa-star" aria-hidden="true"></i></span>
        </div>`;
      $(".selectedFilm").html(gridHtml);

      // close the pop up
      $(".close").on("click", function() {
        $(".selectedFilm").fadeOut();
        $(".bg").fadeToggle();
        $(".view-fav").fadeToggle();
      });
    });
    // if no results display error message
    if (data.results.length == 0) {
      $(".error").html("No data found, search again.");
    }
    // create the film layout
    for (let i = 0; i < data.results.length; i++) {
      const movieResults = data.results[i];
      gridHtml += `<li>
        <img src = "${poster}${movieResults.poster_path}">
    </li>`;
    }

    $(".films").html(gridHtml);
  });

  // click of pop up image - add to favourites div
  $("body").on("click", ".add-fav", function() {
    // get the img src
    let favItems = $(".selectedFilm__poster").attr("src");
    $(".favourite").append(`<img class ="favImg" src ="${favItems}">`);
    // bug - unsure why? duplicate images being displayed on click.
    // removed any duplicated src
    var img = $(".favImg");
    var used = {};

    img.each(function() {
      var src = $(this).attr("src");
      if (used[src]) $(this).remove();
      used[src] = 1;
    });
    localStorage.getItem(favItems);
  });
  localStorage.setItem(favItems);

}
// start app


// use submit to load the data
const form = $(".form");
form.submit(loadData);
