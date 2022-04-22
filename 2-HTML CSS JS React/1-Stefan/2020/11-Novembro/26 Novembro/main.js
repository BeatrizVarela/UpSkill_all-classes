function check() {
    var x = Math.floor((Math.random() * 10) + 1);
    //let x = const random = Math.floor(Math.random() * 10 + 1);
    var i = document.getElementById("input").value;
    console.log(x)
    
    if (i == x) {
        document.getElementById("random").innerHTML = "Good Work";
    } 
    else {
        document.getElementById("random").innerHTML = "Not matched";
    }
   
}