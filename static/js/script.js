const hamburgerMenu = document.querySelector(".hamburger-menu");
const ul = document.querySelector(".nav-list ul");

hamburgerMenu.addEventListener("click", () => {
  hamburgerMenu.classList.toggle("hamburger-rotate");
  ul.classList.toggle("slide-out");
});





