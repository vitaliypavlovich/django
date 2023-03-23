document.addEventListener("DOMContentLoaded", function () {
    function showMessage() {
        let message = "Your message was sent";
        alert(message);
    }

    const button = document.getElementById("submit");

    button.addEventListener("click", showMessage)
});