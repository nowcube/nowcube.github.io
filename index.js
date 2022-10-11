const hamburger = document.querySelector(".hamburger");
const linkGroup = document.querySelector(".link-group");

hamburger.addEventListener("click", navbarChange);

function navbarChange() {
    linkGroup.classList.toggle("active");
}

//设置body背景
var htmlBgs = [];
htmlBgs[0] = "./1.webp";
htmlBgs[1] = "./2.webp";
htmlBgs[2] = "./3.webp";
htmlBgs[3] = "./4.webp";
htmlBgs[4] = "./5.webp";

var randomBgIndex = Math.round(Math.random() * 4);
document.body.style.backgroundImage = "url('" + htmlBgs[randomBgIndex] + "')";