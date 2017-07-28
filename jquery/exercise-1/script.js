to/* You will save your code during today's demos and exercises here. */
//cheat sheet link: https://oscarotero.com/jquery/
$('.frame').hide();
$('.frame').show();

//$('.frame').fadeOut();
//$('.frame').fadeOut(4000,'swing');

$('h5').append("I love cake!");


$('h5').addClass("newColor");



function fadeImage() {
  $('img').fadeToggle();
}

function setupHandlers() {
  $('#android').on('click', fadeImage);
}

$(document).ready(setupHandlers);
