const play = document.querySelector(".play");

play.addEventListener("click", () => {
    let today = new Date();
    sessionStorage.setItem("initMin", today.getMinutes().toString());
    sessionStorage.setItem("initSec", today.getSeconds().toString());
    sessionStorage.setItem("currScore", "0");
})