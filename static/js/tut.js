window.onload = function() {
    document.getElementById('close').onclick = function() {
        // this.parentNode.parentNode.parentNode
        document.getElementById("myform").style.display = "none";
        //     .removeChild(this.parentNode.parentNode);
        // return false;
        document.getElementById("Pop").style.display = "block";
    };
};


function closeForm() {
    document.getElementById("myForm").style.display = "none";
};

function clickB() {

    var formcheck = document.getElementById("myform").style.display;

    if (formcheck != 0 && formcheck != "none") {
        console.log(formcheck, "Form In IF")
        document.getElementById("myForm").style.display = "none";



    } else {
        console.log(formcheck, "Form In else")
        document.getElementById("myform").style.display = "block";
        document.getElementById("Pop").style.display = "none";

    }
};

var recieved = document.getElementById("chatbox");
var button = document.getElementById("Submit");
var recieved_msg = document.getElementById("recieved_msg");

// when button is clicked

button.addEventListener("click", function() {
    // console.log("button clicked");
    var str = recieved.value;
    recieved_msg.innerHTML = str;
    console.log(recieved, recieved_msg, "::::");
    // recieved_msg.value = str;

});

recieved.addEventListener("keyup", function(event) {
    console.log(event.key);
    if (event.key == 13 || event.key == "Enter") {
        // console.log("enter clicked");
        event.preventDefault();
        button.click();
    }
});