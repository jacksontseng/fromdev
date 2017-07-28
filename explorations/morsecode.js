function stringToMorse (string) {
  var array = string.split("");
var array2= [];
  for (var i = 0; i < array.length; i++) {
    if (array[i] === "") {
      array[i++];
    }

      if (array[i] === 'a') {
        array2.push("dot dash ")
      } else if (array[i] === 'b') {
        array2.push("dash dot dot dot ");
      } else if (array[i] === 'c') {
        array2.push("dash dot dash dot ");
      } else if(array[i] === 'd') {
        array2.push("dash dot dot ");
}
  }
  return array2;
}

console.log(stringToMorse("ab"));
