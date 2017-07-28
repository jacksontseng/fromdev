var elevatorLine = [];

function pressFloorNumber(elevatorLine, floornum) {
elevatorLine.unshift(floornum); //unshift instead of push for LIFO instead of FIFO
return "floor " + elevatorLine.length;
}

function goToNextFloor() {
if (elevatorLine.length === 0) {
  return "the elevator is empty!";
}
var i = elevatorLine[1];
elevatorLine.splice(0,1);

return i;
  return
}

function currentLine (ArrayEL){
  if (ArrayEL.length == 0) {
    return "the line is currently empty";
  }
var last =  "The line is currently: ";
  for (i=0; i<ArrayEL.length;i++) {
    last += ("Floor" + ArrayEL[i] + ","); //leaving commas at the end of all items for now.
  }
  return last;
}
