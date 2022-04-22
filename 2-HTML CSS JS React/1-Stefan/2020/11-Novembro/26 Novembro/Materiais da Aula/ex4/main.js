var displayElement = document.getElementById("result-display");
var startingText = displayElement.textContent;
var characterList = startingText.split(""); // ['I', 'n', 'v'...]

var intervalTask = setInterval(revertOne, 500);

function revertOne() {
  var firstCharacter = characterList.shift();
  characterList.push(firstCharacter);
  displayElement.textContent = characterList.join("");
}
