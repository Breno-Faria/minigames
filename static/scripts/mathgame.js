function check(url)
{
	setInterval(() => {
		let today = new Date();
		if (today.getMinutes() === eval(localStorage.getItem("currMin")) && today.getSeconds() === eval(localStorage.getItem("currSec")) + 5)
		{
			window.location.href=url;
		}
	}, 1000)
}

function score()
{
	let mathForm = document.getElementById("mathForm");
	mathForm.addEventListener("submit", () => {
		let answer = document.getElementById("answer").value;

	})
}







function getRandomQuestion()
{
	switch (getRandomNumber(4))
	{
		case 0:
			return `${getRandomNumber(100)} + ${getRandomNumber(100)}`;
		case 1:
			return `${getRandomNumber(100)} - ${getRandomNumber(100)}`;
		case 2:
			return `${getRandomNumber(10)} * ${getRandomNumber(10)}`;
		case 3:
			let num1 = getRandomNumber(10);
            let num2 = getRandomNumber(10);
            while (num1 / num2 !== Math.floor(num1 / num2) || num2 === 0)
            {
                num1 = getRandomNumber(10);
                num2 = getRandomNumber(10);
            }
            return `${num1} / ${num2}`;
        default:
            return "something went wrong";
	}
}

function getRandomNumber(ceiling)
{
	return Math.floor(Math.random() * ceiling);
}