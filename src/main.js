(
    function() {
        let lista = document.getElementById("lista"),
            tareaInput = document.getElementById("tareaInput"),
            gastoInput = document.getElementById("gastoInput"),
            btnNuevaTarea = document.getElementById("btn-agregar");
        
        let agregarTarea = function() {
            let tarea = tareaInput.value,
                gasto = gastoInput.value,
                nuevaTarea = document.createElement("li"),
                enlace = document.createElement("a"),
                contenido = document.createTextNode(tarea + ": " + gasto);
            
            if (tarea === "" || gasto === "") {
                tareaInput.setAttribute("placeholder", "Datos incompletos");
                tareaInput.className = "error";
                return false;
            }
            
            enlace.appendChild(contenido);
            enlace.setAttribute("href", "#");
            nuevaTarea.appendChild(enlace);
            lista.appendChild(nuevaTarea);

            tareaInput.value = "";
            gastoInput.value = "";
            
            for (let i = 0; i < lista.children.length; i++) {
                lista.children[i].addEventListener("click", function() {
                    this.parentNode.removeChild(this);
                });
            }
        };

        let comprobarInput = function() {
            tareaInput.className = "";
            tareaInput.setAttribute("placeholder", "Nombre");
            gastoInput.setAttribute("placeholder", "Gasto");
        };

        let eliminarTarea = function() {
            this.parentNode.removeChild(this);
        };

        btnNuevaTarea.addEventListener("click", agregarTarea);
        tareaInput.addEventListener("click", comprobarInput);

        for (let i = 0; i < lista.children.length; i++) {
            lista.children[i].addEventListener("click", eliminarTarea);
        }
    } ()
)