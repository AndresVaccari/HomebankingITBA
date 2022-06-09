const API_URL = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";
const xmlHttp = new XMLHttpRequest();
const HTMLResponse = document.getElementById("dolar");
const ul = document.createElement("ul");
const tiposDolar = ["Dolar Oficial", "Dolar Blue", "Dolar turista"];

(async function getData() {
  const response = await fetch(API_URL);
  const data = await response.json();
  data.forEach((tipo) => {
    if (tiposDolar.includes(tipo.casa.nombre)) {
      const li = document.createElement("li");
      const p = document.createElement("p");
      const texto = document.createTextNode(
        `${tipo.casa.nombre} - Compra: ${tipo.casa.compra} - Venta: ${tipo.casa.venta}`
      );
      p.appendChild(texto);
      li.appendChild(p);
      li.className = "list-group-item";
      ul.appendChild(li);
    }
  });
  ul.className = "list-group";
  HTMLResponse.appendChild(ul);
})();
