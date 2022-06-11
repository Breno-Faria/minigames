const play = document.querySelector(".play");

play.addEventListener("click", () => {
    let today = new Date();
    localStorage.setItem("currSec", today.getSeconds());
    localStorage.setItem("currMin", today.getMinutes());
})