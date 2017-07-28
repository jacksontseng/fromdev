function square(pos) {
if (pos <= 0) { //tests that chess square is valid.
  return "invalid square, less than or equal to 0";
}


result =Math.pow(2, (pos-1))
return result;
}
console.log(square(3));


function total (pos) {
  var total = 0;
  for (var i =1; i < pos+1; i++) {
   total += square(i);
  }
    return total;
}

console.log(total(3));
