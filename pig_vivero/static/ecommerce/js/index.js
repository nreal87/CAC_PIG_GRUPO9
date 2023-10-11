let menu = document.getElementById("menu__celular");
let nav = document.getElementById("menu__icono");
let hamburguesa = document.getElementById("menu-hamburguesa");
let cruz = document.getElementById("menu-cruz");
let item = document.querySelectorAll(".menu_li");

nav.addEventListener("click", (e) => {
  menu.classList.toggle("mostrar");
  hamburguesa.classList.toggle("close");
  cruz.classList.toggle("close");
});
item.forEach((i) => {
  i.addEventListener("click", (e) => {
    menu.classList.toggle("mostrar");
    hamburguesa.classList.toggle('close');
    cruz.classList.toggle('close');
  });
});