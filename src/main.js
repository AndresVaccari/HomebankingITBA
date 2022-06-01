(
    function() {
        let lista = document.getElementById("lista"),
            nombreInput = document.getElementById("nombreInput"),
            gastoInput = document.getElementById("gastoInput"),
            gastoTotal = document.getElementById("gastoTotal"),
            gastoDividido = document.getElementById("gastoDividido"),
            total = 0;
            contador = 0;
            btnNuevoNombre = document.getElementById("btn-agregar");

        let agregarNombre = function() {
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
            }
            
            enlace.appendChild(contenido);
            enlace.setAttribute("href", "#");
            nuevoNombre.appendChild(enlace);
            lista.appendChild(nuevoNombre);
            nuevoNombre.classList.add("list-group-item");

            nombreInput.value = "";
            gastoInput.value = "";

            total+= parseInt(gasto);
            contador++;
            gastoDividido.innerHTML = "Cada uno tendra que pagar: $" + (total / contador);
            gastoTotal.innerHTML = "Total: $" + total;
            
            for (let i = 0; i < lista.children.length; i++) {
                lista.children[i].addEventListener("click", function() {
                    let totalAEliminar = parseInt(lista.children[i].textContent.split(":")[1]);
                    total-= parseInt(totalAEliminar);
                    contador--;
                    if (total != 0) {
                        gastoDividido.innerHTML = "Cada uno tendra que pagar: $" + (total / contador);
                        gastoTotal.innerHTML = "Total: $" + total;
                    } else {
                        gastoDividido.innerHTML = "No hay nadie";
                        gastoTotal.innerHTML = "Total: $" + 0;
                    }
                    
                    this.parentNode.removeChild(this);
                });
            }


        };

        let comprobarInput = function() {
            nombreInput.className = "";
            gastoInput.className = "";
            nombreInput.setAttribute("placeholder", "Nombre");
            gastoInput.setAttribute("placeholder", "Gasto");
        };

        btnNuevoNombre.addEventListener("click", agregarNombre);
        nombreInput.addEventListener("click", comprobarInput);
        gastoInput.addEventListener("click", comprobarInput);

    } ()
)