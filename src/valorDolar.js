const API_URL = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";
const HTMLResponse = document.getElementById("dolar");
const ul = document.createElement("ul");
const tiposDolar = ["Dolar Oficial", "Dolar Blue", "Dolar turista"];
const dolarSoloVenta = ["Dolar turista"];
const imagenesDolar = [
  "img/dolar/oficial.png",
  "img/dolar/blue.png",
  "img/dolar/turista.png",
];

(async function getData() {
  const response = await fetch(API_URL);
  const data = await response.json();
  let cont = 0;
  data.forEach((tipo) => {
    if (tiposDolar.includes(tipo.casa.nombre)) {
      const li = document.createElement("li");
      const p = document.createElement("p");
      const img = document.createElement("img");
      let texto;
      img.src = imagenesDolar[cont];
      img.height = "20";
      if (dolarSoloVenta.includes(tipo.casa.nombre)) {
        texto = document.createTextNode(
          `${tipo.casa.nombre} - Venta: ${tipo.casa.venta}  `
        );
      } else {
        texto = document.createTextNode(
          `${tipo.casa.nombre} - Compra: ${tipo.casa.compra} - Venta: ${tipo.casa.venta}  `
        );
      }

      p.appendChild(texto);
      p.appendChild(img);
      cont++;
      li.appendChild(p);
      li.className = "list-group-item";
      ul.appendChild(li);
    }
  });
  ul.className = "list-group";
  HTMLResponse.appendChild(ul);
})();
