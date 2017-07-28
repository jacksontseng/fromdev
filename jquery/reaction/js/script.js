var d = new Date();
var n  = d.getTime();
var random = Math.random()*10*1000; //0 to 10 in milliseconds
var start = n + random;





setTimeout(start,random);

function start () {

}

function setupHandlers() {
  $('.frame').hide();
  $('.frame').show(random);
  console.log(random);
}
$('#android').on('click', record());

function record() {
var d1= new Date();
var n1 = d1.getTime();

  console.log(n1);
}

$(document).ready(setupHandlers);
