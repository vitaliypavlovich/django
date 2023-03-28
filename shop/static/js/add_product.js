document.addEventListener("DOMContentLoaded", function () {
    function showMessage() {
        let message = "Product was add";
        alert(message);
    }

    const button = document.getElementById("save");

    button.addEventListener("click", showMessage)
});