function openForm() {
    // console.log("OPen form")
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

var input = document.getElementById("chatbox")
input.addEventListener("keyup", function(event) {
    if (event.key == 13) {
        event.preventDefault();
        document.getElementById("Submit").click();
    }
})

function submit() {
    console.log(input);
}