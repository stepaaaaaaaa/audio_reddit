function showPopupMessage() {
    var messageElement = document.getElementById("message");
    messageElement.textContent = "Нажмите на 3 точки чтобы скачать запись";
    messageElement.style.display = "block";
}

document.addEventListener("DOMContentLoaded", function() {
    var button = document.getElementById("stopButton");
    button.addEventListener("click", showPopupMessage);
  });