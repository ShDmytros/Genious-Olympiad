const form = document.getElementById("playForm");
const loadingScreen = document.getElementById("loadingScreen");

const symbols = document.getElementById("text_length");
// const  = document.getElementById("article");


form.addEventListener("submit", function () {
  loadingScreen.style.display = "flex";
});

form.addEventListener("input", function () {
  symbols.innerHTML = form.querySelector("#explaining").value.length;
});
