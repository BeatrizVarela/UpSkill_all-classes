const random = Math.floor(Math.random() * 10 + 1);
console.log(random);

// function adivinhaNumero() {
//   let chosenNumber = prompt("Adivinha o número");

//   while (chosenNumber != random) {
//     alert("Errado tente outra vez");
//     chosenNumber = prompt("Adivinha o número");
//   }

//   if (chosenNumber == random) {
//     alert("Acertou");
//   }
// }

// onpageshow = adivinhaNumero;
let submitButton = document.getElementById("submit-button");
submitButton.addEventListener("click", function (event) {
  //   event.preventDefault();
  let chosenNumber = document.forms.numberguessing.number.value;
  if (random == chosenNumber) {
    alert("Acertou");
  } else {
    alert("Errado");
  }
});
