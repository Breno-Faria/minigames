function check(url)
{
    setInterval(() => {
        let today = new Date();
        if (today.getMinutes() === eval(localStorage.getItem("currMin")) && today.getSeconds() === eval(localStorage.getItem("currSec")) + 5)
        {
            window.location.href=url
        }
    }, 1000)
}