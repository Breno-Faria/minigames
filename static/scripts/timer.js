const play = document.querySelector(".play");

play.addEventListener("click", () => {
    let today = new Date();
    sessionStorage.setItem("currSec", today.getSeconds());
    sessionStorage.setItem("currMin", today.getMinutes());
    sessionStorage.setItem("currScore", "0");
})