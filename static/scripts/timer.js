const play = document.querySelector(".play");

play.addEventListener("click", () => {
    let today = new Date();
    sessionStorage.setItem("initMin", today.getMinutes().toString());
    sessionStorage.setItem("initSec", today.getSeconds().toString());
    sessionStorage.setItem("currScore", "0");
})

const play2 = document.querySelector(".play2");

play2.addEventListener("click", () => {
    sessionStorage.setItem("currScore", "0");
})