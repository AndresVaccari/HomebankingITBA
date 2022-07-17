import json
import os

from clienteBlack import ClienteBlack
from clienteClassic import ClienteClassic
from clienteGold import ClienteGold
from razon import Razon

ARCHIVOS = (
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosBlack.json"),
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosClassic.json"),
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosGold.json"),
)

DIRECCION_HTML = os.path.join(os.path.dirname(os.path.realpath(__file__)), "transaccion.html")


def generarClientes(*args):
    clientes = []
    for direccion in args:
        with open(direccion, "r") as archivo:
            cliente = json.load(archivo)
            if cliente["tipo"] == "BLACK":
                clientes.append(ClienteBlack(cliente))
            elif cliente["tipo"] == "GOLD":
                clientes.append(ClienteGold(cliente))
            else:
                clientes.append(ClienteClassic(cliente))
            print("Cliente creado")
    return clientes


def crearHTML():
    archivoHtml = open(DIRECCION_HTML, "w")
    archivoHtml.write(
        f"""
            <!DOCTYPE html>
            <head>
            <html lang="en">
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous" />
            </head>
            <body class="container">
        """
    )
    for cliente in clientes:
        print(cliente)
        archivoHtml.write(
            f"""
                <h2 class="mt-5">{cliente.getNombre()} {cliente.getApellido()}</h2>
                <p>Numero de cliente: <strong>{cliente.getNumeroCliente()}</strong></p>
                <p>DNI: <strong>{cliente.getDni()}</strong></p>
                <p>Direccion: <strong>{cliente.getDireccion('calle')} {cliente.getDireccion('numero')} ({cliente.getDireccion('ciudad')}/{cliente.getDireccion('provincia')}/{cliente.getDireccion('pais')})</strong></p>

                <h3>Transacciones</h3>
                <table class="table table-light">
                    <thead>
                        <tr>
                          <th scope="col">Fecha</th>
                          <th scope="col">Operacion</th>
                          <th scope="col">Estado</th>
                          <th scope="col">Monto</th>
                          <th scope="col">Razon</th>
                        </tr>
                    </thead>
                    <tbody>
            """
        )
        diccTransacciones = cliente.getTransacciones()
        for transaccion in diccTransacciones:
            razon = Razon(transaccion, cliente)
            archivoHtml.write(
                f"""
                    <tr>
                        <td>{transaccion["fecha"]}</td>
                        <td>{transaccion["tipo"]}</td>
                        <td>{transaccion["estado"]}</td>
                        <td>{transaccion["monto"]}</td>
                """
            )
            if razon.getRazon() != "OK":
                archivoHtml.write(f"<td>{razon.getRazon()}</td>")
            else:
                archivoHtml.write("<td></td>")
            archivoHtml.write("</tr></tbody>")
        archivoHtml.write("</table>")
    archivoHtml.write("</body>")
    print("Se genero el archivo transaccion.html")
    archivoHtml.close()


if __name__ == "__main__":
    print("Iniciando segmentacion de clientes")
    clientes = generarClientes(*ARCHIVOS)
    print("Se generaron los clientes")
    archivoHtml = crearHTML()
