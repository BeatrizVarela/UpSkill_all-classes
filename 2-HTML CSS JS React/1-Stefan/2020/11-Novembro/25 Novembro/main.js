function myFunction() {
var green = document.getElementsByClassName("greenp");
for (var i = 0; i < green.length; i++) {
    green[i].style.color = 'green';
    }

var elements = document.getElementsByTagName('p');
for (var i = 0; i < elements.length; i++) {
    elements[i].style.fontSize = "150%";
    }

var red = document.getElementsByTagName('h1');
for (var i = 0; i < red.length; i++) {
    red[i].style.color = 'red';
    }
}
