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
      const a = document.createElement("a");
      const texto = document.createTextNode(tipo.casa.nombre);
      a.appendChild(texto);
      a.setAttribute("href", "#");
      li.appendChild(a);
      ul.appendChild(li);
    }
  });
  HTMLResponse.appendChild(ul);
})();
