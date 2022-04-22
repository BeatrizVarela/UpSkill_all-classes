$(document).ready(function () {
  var squareIn = true;
  $("#switch").click(slideStuff);

  $("#switch").on("click", function () {
    console.log("quadrado alterado");
  });

  $("#switch").off("click", slideStuff);
});

function slideStuff(event) {
  if (squareIn) {
    //   $("#square").fadeTo("slow", 0);
    $("#square").slideUp();
  } else {
    //   $("#square").fadeIn(5000);
    $("#square").slideDown();
  }
  squareIn = !squareIn;
}
