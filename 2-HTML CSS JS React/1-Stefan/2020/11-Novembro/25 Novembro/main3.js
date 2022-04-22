var value = 0

var valueDisplay = document.getElementById("value-display");
var addB = document.getElementById("add");
var subB = document.getElementById("sub");

addB.addEventListener("click",function () {
    value ++;
    valueDisplay.innerHTML = value.toString();
});

subB.addEventListener("click",function () {
    value --;
    valueDisplay.innerHTML = value.toString();
});