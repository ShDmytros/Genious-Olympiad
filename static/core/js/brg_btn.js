const burger = document.getElementById("burger");
const menu = document.getElementById("menu");
let isClicked = false;

burger.addEventListener("click", () => {
  if (!isClicked) {
    menu.classList.remove("hidden");
  } else {
    menu.classList.add("hidden");
  }

  isClicked = !isClicked;
});
