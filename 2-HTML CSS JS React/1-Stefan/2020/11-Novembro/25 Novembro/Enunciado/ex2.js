var value = 0;

var valueDisplay = document.getElementById("value-display");
var addBtn = document.getElementById("addBtn");
var subtractBtn = document.getElementById("subtractBtn");

addBtn.addEventListener("click",function () {
    value ++;
    valueDisplay.innerHTML = value.toString();
});

subtractBtn.addEventListener("click",function () {
    value --;
    valueDisplay.innerHTML = value.toString();
});