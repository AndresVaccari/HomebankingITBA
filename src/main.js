(function () {
  let lista = document.getElementById("lista"),
    nombreInput = document.getElementById("nombreInput"),
    gastoInput = document.getElementById("gastoInput"),
    gastoTotal = document.getElementById("gastoTotal"),
    gastoDividido = document.getElementById("gastoDividido"),
    total = 0;
  contador = 0;
  btnEnviar = document.getElementById("btn-enviar");

  let agregarNombre = function () {
    let nombre = nombreInput.value,
      gasto = gastoInput.value,
      nuevoNombre = document.createElement("li"),
      enlace = document.createElement("a"),
      contenido = document.createTextNode(nombre + ": " + gasto);

    if (nombre === "" || gasto === "") {
      nombreInput.setAttribute("placeholder", "Datos incompletos");
      gastoInput.setAttribute("placeholder", "Datos incompletos");
      nombreInput.className = "error";
      gastoInput.className = "error";
      return false;
    }
    if (isNaN(gasto)) {
      gastoInput.value = "";
      gastoInput.setAttribute("placeholder", "Debe ingresar un numero");
      gastoInput.className = "error";
      return false;
    } else if (parseInt(gasto) <= 0) {
      gastoInput.value = "";
      gastoInput.setAttribute("placeholder", "El gasto debe ser mayor a 0");
      gastoInput.className = "error";
      return false;
    }

    enlace.appendChild(contenido);
    enlace.setAttribute("href", "#");
    nuevoNombre.appendChild(enlace);
    lista.appendChild(nuevoNombre);
    nuevoNombre.classList.add("list-group-item");

    nombreInput.value = "";
    gastoInput.value = "";

    lista.children[contador].addEventListener("click", function () {
      let totalAEliminar = parseInt(this.innerText.split(":")[1]);
      console.log(totalAEliminar);
      total -= totalAEliminar;
      contador--;
      if (total != 0) {
        gastoDividido.innerHTML =
          "<b>Cada uno tendra que pagar</b>: $" + total / contador;
        gastoTotal.innerHTML = "<b>Total</b>: $" + total;
      } else {
        gastoDividido.innerHTML = "<b>No hay nadie</b>";
        gastoTotal.innerHTML = "<b>Total</b>: $" + 0;
      }
      this.parentNode.removeChild(this);
    });

    total += parseInt(gasto);
    contador++;
    gastoDividido.innerHTML =
      "<b>Cada uno tendra que pagar</b>: $" + total / contador;
    gastoTotal.innerHTML = "<b>Total</b>: $" + total;
  };

  let comprobarInput = function () {
    nombreInput.className = "";
    gastoInput.className = "";
    nombreInput.setAttribute("placeholder", "Nombre");
    gastoInput.setAttribute("placeholder", "Gasto");
  };

  btnEnviar.addEventListener("click", agregarNombre);
  nombreInput.addEventListener("click", comprobarInput);
  gastoInput.addEventListener("click", comprobarInput);
})();
