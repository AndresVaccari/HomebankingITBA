(
    function() {
        let lista = document.getElementById("lista"),
            tareaInput = document.getElementById("tareaInput"),
            gastoInput = document.getElementById("gastoInput"),
            gastoTotal = document.getElementById("gastoTotal"),
            gastoDividido = document.getElementById("gastoDividido"),
            total = 0;
            contador = 0;
            btnNuevaTarea = document.getElementById("btn-agregar");
        
        let agregarTarea = function() {
            let tarea = tareaInput.value,
                gasto = gastoInput.value,
                nuevaTarea = document.createElement("li"),
                enlace = document.createElement("a"),
                contenido = document.createTextNode(tarea + ": " + gasto);
            
            if (tarea === "" || gasto === "") {
                tareaInput.setAttribute("placeholder", "Datos incompletos");
                gastoInput.setAttribute("placeholder", "Datos incompletos");
                tareaInput.className = "error";
                gastoInput.className = "error";
                return false;
            } 
            if (isNaN(gasto)) {
                tareaInput.setAttribute("placeholder", "Debe ingresar un numero");
                gastoInput.setAttribute("placeholder", "Debe ingresar un numero");
                tareaInput.className = "error";
                gastoInput.className = "error";
                return false;
            }
            
            enlace.appendChild(contenido);
            enlace.setAttribute("href", "#");
            nuevaTarea.appendChild(enlace);
            lista.appendChild(nuevaTarea);

            tareaInput.value = "";
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
            tareaInput.className = "";
            gastoInput.className = "";
            tareaInput.setAttribute("placeholder", "Nombre");
            gastoInput.setAttribute("placeholder", "Gasto");
        };

        btnNuevaTarea.addEventListener("click", agregarTarea);
        tareaInput.addEventListener("click", comprobarInput);
        gastoInput.addEventListener("click", comprobarInput);

    } ()
)