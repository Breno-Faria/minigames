const play = document.querySelector(".play");

play.addEventListener("click", () => {
    sessionStorage.setItem("currScore", "0");
})