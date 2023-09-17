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


let opcProvicia = document.getElementById("provincia");
let opcCiudad = document.getElementById("ciudad");

/*Funcion para buscar todas las provincias*/
let fetchProvicias = () => {
  return fetch('https://apis.datos.gob.ar/georef/api/provincias')
    .then(response => response.json())
    .catch(error => console.log(`Error al buscar las provincias. ${error}`));
}
/* Configuracion para que el selector de provincia se cargue cuando hago click y esta vacia*/

opcProvicia.addEventListener('click', async function (event) {

  event.preventDefault();
  /* Con este if buscamos que las provincias se carguen una sola vez */

  if (opcProvicia.length === 0) {

    const listaProvincias = await fetchProvicias();/*invoco a la fc para cargar las provincias*/

    /*Creo un string con el html para agregar todas provincias*/
    if (listaProvincias) {
      for (let i = 0; i < listaProvincias.cantidad; i++) {

        let newOption = document.createElement("option");
        newOption.text = `${listaProvincias.provincias[i].nombre}`;
        opcProvicia.add(newOption);
      }
    }
  }
})

/* Funcion para traer las ciudades le la provincia seleccionada*/
let fetchCiudades = (buscarProv) => {
  return fetch(buscarProv)
    .then(response => response.json())
    .catch(error => console.log(error));
}

/* Funciones para cargar las ciudades de la provincia seleccionada*/
opcProvicia.addEventListener('change', async function (event) {
  event.preventDefault();

  let provinciaSeleccionada = opcProvicia.options[opcProvicia.selectedIndex].value;
  let BuscarProvincia = `https://apis.datos.gob.ar/georef/api/localidades?provincia=${provinciaSeleccionada}`;
  const listaCiudades = await fetchCiudades(BuscarProvincia);

  document.querySelector('#ciudad').innerHTML = '';

  if (listaCiudades) {
    for (let i = 0; i < listaCiudades.cantidad; i++) {

      let newOption = document.createElement("option");
      newOption.text = `${listaCiudades.localidades[i].nombre}`;
      opcCiudad.add(newOption);
    }

  }
})

/*Validacion del formulario*/

function validacionFormulario() {

  let nombre = document.getElementById('nombre').value;
  let email = document.getElementById('email').value;
  let provincia = document.getElementById('provincia').selectedIndex;
  let ciudad = document.getElementById('ciudad').selectedIndex;
  let mensaje = document.getElementById('mensaje').value;

  //Campos no vacios
  if (nombre === '' || email === '' || ciudad === -1 || provincia === -1 || mensaje === '') {
    alert("Debe completar todos los campos del formulario");
    return false;
  }

  //Formato correo

  var expresion = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
  if (!expresion.test(email)) {
    alert("el email ingresado es incorrecto, intente nuevamente");
    return false;
  }

  return true;
}

/*Funciones para poder registrar los datos del formulario*/

const formulario = document.getElementById('form');
formulario.addEventListener('submit', async function (event) {
  event.preventDefault();

  if (validacionFormulario()) {

    const datoForm = new FormData(formulario);

    try {
      const response = await fetch('https://formspree.io/f/moqzbkod', {
        method: 'POST',
        body: datoForm,
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        alert("Se envio el formulario con éxito.");
        console.log(datoForm);

        // Restablecer el formulario solo si la respuesta es exitosa
        formulario.reset();
        document.querySelector('#ciudad').innerHTML = '';
        document.querySelector('#provincia').innerHTML = '';

      } else {
        alert("Se produjo un error al enviar el formulario. Pruebe de nuevo.");
      }
    } catch (error) {
      alert("Se produjo un error al enviar el formulario. Pruebe de nuevo");
      console.log(error);
    }
  }
});

