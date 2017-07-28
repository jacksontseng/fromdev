function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}
function fadeInWhenClicked() {
  $("#pig").fadeIn();
}
function fadeOutWhenClicked() {
  $("#pig").fadeOut();
}

function scale() {
  $("#pig").animate({width: '150%'});
}
function scaledown() {
  $("#pig").animate({width: '50%'});
}

function flyright() {
  $("#pig").animate({right:'25%', opacity:'0.5'}, "slow");
$("#pig").animate({right:'75%',opacity:'1'},"slow");

}
function flyleft() {
  $("#pig").animate({right: '75%'});
}
function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#fadeOPig").click(fadeOutWhenClicked);
    $("#fadeIPig").click(fadeInWhenClicked);
    $("#ScalePig").click(scale);
    $("#scaleDownPig").click(scaledown);
    $("#flyrightpig").click(flyright);
    $("#flyleftpig").click(flyleft);

$("#pig").click(flyright);//calls fly right function on click
}

$(document).ready(setup);
