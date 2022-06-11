function check()
{
    setInterval(() => {
        let today = new Date();
        if (today.getMinutes() === eval(localStorage.getItem("currMin")) + 2 && today.getSeconds() === eval(localStorage.getItem("currSec")))
        {
            alert("ayo");
        }
    }, 1000)
}

check()