document.addEventListener("DOMContentLoaded", function() {
    const productosTable = document.getElementById("productosTable");
    const productosBody = document.getElementById("productosBody");
    const formulario = document.getElementById("formulario");
    const codigoInput = document.getElementById("codigo");
    const nombreInput = document.getElementById("nombre");
    const descripcionInput = document.getElementById("descripcion");
    const precioInput = document.getElementById("precio");
    const stockInput = document.getElementById("stock");
    const categoriaInput = document.getElementById("categoria");
    const imagenInput = document.getElementById("imagen");
    const btnAgregar = document.getElementById("btnAgregar");
  
    // Agregar evento de clic al botón "Actualizar" del formulario de edición
    const btnActualizar = document.getElementById("btnActualizar");
    btnActualizar.addEventListener("click", actualizarProducto);
  
    // Agregar evento de clic al botón "Cancelar" del formulario de edición
    const btnCancelar = document.getElementById("btnCancelar");
    btnCancelar.addEventListener("click", cancelarEdicion);
  
    // Agregar evento de clic al botón "Cerrar" de la ventana emergente
    const btnCerrar = document.getElementById("btnCerrar");
    btnCerrar.addEventListener("click", ocultarFormularioEditar);
  
    // Obtener la lista de productos desde el backend
    function obtenerProductos() {
      fetch("http://127.0.0.1:5000/productos")
      // fetch("http://luisescobar.pythonanywhere.com/productos")
      
        .then((response) => response.json())
        .then((data) => {
          //mostrarProductos(data);
          mostrarProductos(data.productos);
        })
        .catch((error) => console.log(error));
    }
  
    // Mostrar los productos en la tabla
    function mostrarProductos(productos) {
      // Limpiar contenido anterior de la tabla
      productosBody.innerHTML = "";
      
      // Generar filas para cada producto
      productos.forEach((producto) => {
        const row = document.createElement("tr");
        row.setAttribute("data-codigo", producto.codigo);
  
        const codigoCell = document.createElement("td");
        codigoCell.textContent = producto.codigo;
        row.appendChild(codigoCell);
  
        const nombreCell = document.createElement("td");
        nombreCell.textContent = producto.nombre;
        row.appendChild(nombreCell);
  
        const descripcionCell = document.createElement("td");
        descripcionCell.textContent = producto.descripcion;
        row.appendChild(descripcionCell);
  
        const precioCell = document.createElement("td");
        precioCell.textContent = producto.precio;
        row.appendChild(precioCell);
  
        const stockCell = document.createElement("td");
        stockCell.textContent = producto.stock;
        row.appendChild(stockCell);
  
        const categoriaCell = document.createElement("td");
        categoriaCell.textContent = producto.categoria;
        row.appendChild(categoriaCell);
  
        const imagenCell = document.createElement("td");
        const imagen = document.createElement("img");
        imagen.src = producto.imagen;
        imagen.alt = producto.nombre;
        imagenCell.appendChild(imagen);
        row.appendChild(imagenCell);
  
        const accionesCell = document.createElement("td");
  
        const btnEditar = document.createElement("button");
        btnEditar.textContent = "Editar";
        btnEditar.addEventListener("click", editarProducto);
        accionesCell.appendChild(btnEditar);
  
        const btnEliminar = document.createElement("button");
        btnEliminar.textContent = "Eliminar";
        btnEliminar.addEventListener("click", eliminarProducto);
        accionesCell.appendChild(btnEliminar);
  
        row.appendChild(accionesCell);
  
        productosBody.appendChild(row);
      });
    }
  
    // Agregar un nuevo producto
    function agregarProducto() {
      const producto = {
        codigo: codigoInput.value,
        nombre: nombreInput.value,
        descripcion: descripcionInput.value,
        precio: precioInput.value,
        stock: stockInput.value,
        categoria: categoriaInput.value,
        imagen: imagenInput.value,
      };
  
       fetch("http://127.0.0.1:5000/producto", {
        // fetch("http://luisescobar.pythonanywhere.com/producto", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(producto),
      })
        .then((response) => response.json())
        .then((data) => {
          obtenerProductos();
          limpiarFormulario();
        })
        .catch((error) => console.log(error));
    }
  
    // Editar producto
    function editarProducto(event) {
      if (
        event.target.tagName === "BUTTON" &&
        event.target.textContent === "Editar"
      ) {
        const row = event.target.closest("tr");
        const codigo = row.dataset.codigo;
  
        // Obtener los datos del producto de la fila correspondiente
        const nombre = row.querySelector("td:nth-child(2)").textContent;
        const descripcion = row.querySelector("td:nth-child(3)").textContent;
        const precio = row.querySelector("td:nth-child(4)").textContent;
        const stock = row.querySelector("td:nth-child(5)").textContent;
        const categoria = row.querySelector("td:nth-child(6)").textContent;
        const imagen = row.querySelector("img").src;
  
        // Cargar los datos del producto en el formulario de edición
        const codigoEditarInput = document.getElementById("codigoEditar");
        const nombreEditarInput = document.getElementById("nombreEditar");
        const descripcionEditarInput = document.getElementById("descripcionEditar");
        const precioEditarInput = document.getElementById("precioEditar");
        const stockEditarInput = document.getElementById("stockEditar");
        const categoriaEditarInput = document.getElementById("categoriaEditar");
        const imagenEditarInput = document.getElementById("imagenEditar");
  
        codigoEditarInput.value = codigo;
        nombreEditarInput.value = nombre;
        descripcionEditarInput.value = descripcion;
        precioEditarInput.value = precio;
        stockEditarInput.value = stock;
        categoriaEditarInput.selectedIndex = categoria;
        imagenEditarInput.value = imagen;
  
        // Mostrar el formulario de edición
        ventanaEmergente.style.display = "flex";
        formularioEditar.style.display = "block";
  
        // Agregar evento de clic al botón "Actualizar" del formulario de edición
        const btnActualizar = document.getElementById("btnActualizar");
        btnActualizar.addEventListener("click", actualizarProducto);
  
        // Agregar evento de clic al botón "Cancelar" del formulario de edición
        const btnCancelar = document.getElementById("btnCancelar");
        btnCancelar.addEventListener("click", ocultarFormularioEditar);
      }
    }
  
    // Actualizar producto
    function actualizarProducto() {
      const codigo = document.getElementById("codigoEditar").value;
      const nombre = document.getElementById("nombreEditar").value;
      const descripcion = document.getElementById("descripcionEditar").value;
      const precio = document.getElementById("precioEditar").value;
      const stock = document.getElementById("stockEditar").value;
      const categoria = document.getElementById("categoriaEditar").value;
      const imagen = document.getElementById("imagenEditar").value;
  
      const producto = {
        codigo: codigo,
        nombre: nombre,
        descripcion: descripcion,
        precio: precio,
        stock: stock,
        categoria: categoria,
        imagen: imagen,
      };
  
        fetch(`http://127.0.0.1:5000/update/${codigo}`, {
        // fetch(`http://luisescobar.pythonanywhere.com/update/${codigo}`, {
        
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(producto),
      })
        .then((response) => response.json())
        .then((data) => {
          obtenerProductos();
          limpiarFormulario();
          ocultarFormularioEditar();
        })
        .catch((error) => console.log(error));
    }
     // Cancelar la edición de un producto
     function cancelarEdicion() {
      limpiarFormulario();
      ocultarFormularioEditar();
    }
  
    // Ocultar la ventana emergente y el formulario de edición
    function ocultarFormularioEditar() {
      ventanaEmergente.style.display = "none";
      formularioEditar.style.display = "none";
    }
  
     // Eliminar un producto existente------------------------------------
     function eliminarProducto(event) {
      const codigo = event.target.closest("tr").dataset.codigo;
      
      fetch(`http://127.0.0.1:5000/delete/${codigo}`, {
        // fetch(`http://luisescobar.pythonanywhere.com/delete/${codigo}`, {
        method: "DELETE",
      })
        .then((response) => response.json())
        .then((data) => {
          obtenerProductos();
          limpiarFormulario();
        })
        .catch((error) => console.log(error));
    }
  
    // Limpiar el formulario
    function limpiarFormulario() {
      codigoInput.value = "";
      nombreInput.value = "";
      descripcionInput.value = "";
      precioInput.value = "";
      stockInput.value = "";
      categoriaInput.value = "";
      imagenInput.value = "";
    }
  
    // Evento para agregar un nuevo producto
    btnAgregar.addEventListener("click", agregarProducto);
  
    // Obtener los productos al cargar la página
    obtenerProductos();
  });