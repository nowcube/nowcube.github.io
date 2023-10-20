const hamburger = document.querySelector(".hamburger");
const linkGroup = document.querySelector(".link-group");

hamburger.addEventListener("click", navbarChange);

function navbarChange() {
    linkGroup.classList.toggle("active");
}
