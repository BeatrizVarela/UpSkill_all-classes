$(document).ready(function () {
  var squareIn = true;
  $("#switch").click(function () {
    if (squareIn) {
      // $("#square").fadeOut("slow");

      // $("#square").fadeTo("slow", 0.5);
      // $("#square").fadeTo("slow", 0);

      // $("#square").slideUp("fast");

      // $("#square").animate({ height: "400pt" }, "slow");

      $("#square").slideUp();
    } else {
      // $("#square").fadeIn("slow");

      // $("#square").slideDown("slow");

      // $("#square").animate({ height: "0" }, "slow");

      $("#square").slideDown();
    }
    squareIn = !squareIn;

    $("#switch").on("click", function () {
      console.log("quadrado alterado");
    });
  });
});
