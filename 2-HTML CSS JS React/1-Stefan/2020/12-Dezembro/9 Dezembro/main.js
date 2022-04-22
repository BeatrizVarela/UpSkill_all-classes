/* var myVanillaVariable = 3;

for (let i = 0; i < myVanillaVariable; i++) {
  i++;
}

console.log('myVanillaVariable: ${myVanillaVariable}');
// console.log('i: ${i}');
*/

/*
function myFunction(argument) {
  // do something
}
*/

/*
const myFunction = (argument) => argument * 2;
*/

/*
const Function = (argument) => {
  console.log("Hello World");
    console.log("Hello Aagin");
}

Function ()
*/

/*
const myData = [
  {
  temperatura: 50,
  idSensor: 123456789012,
  humidade: 90,
  clorofila: "50%"
}
]

const converteTemperatura = ({temperatura}) => {
  console.log(temperatura * 0.2);
}

myData.forEach((dado) => {
  converteTemperatura (dado)
});
*/

/*
const myData = [
    {
    temperatura: 50,
    idSensor: 123456789012,
    humidade: 90,
    clorofila: "50%"
  }]
  
  const {temperatura} = myData[0];
  console.log(temperatura)
*/

/*
const listaDeTresNumeros = [1,2,3];

const somaTres = (numero1, numero2, numero3) => {
  return numero1 + numero2 + numero3;
}

console.log(somaTres(...listaDeTresNumeros));
*/

const listaDeTresNumeros = [1, 2];
const outraListaDeTresNumeros = listaDeTresNumeros;

outraListaDeTresNumeros[0] = 3;
console.log("listaDeTresNumeros: " + listaDeTresNumeros);
console.log("outraListaDeTresNumeros: " + outraListaDeTresNumeros);
