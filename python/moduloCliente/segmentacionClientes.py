import json
from clienteBlack import ClienteBlack
from clienteClassic import ClienteClassic
from clienteGold import ClienteGold
from razon import Razon

ARCHIVOS = (
    "ejemplosJson/eventosBlack.json",
    "ejemplosJson/eventosClassic.json",
    "ejemplosJson/eventosGold.json",
)


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
    archivoHtml = open("transaccion.html", "w")
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
                <ul class="list-group">
            """
        )
        diccTransacciones = cliente.getTransacciones()
        for transaccion in diccTransacciones:
            razon = Razon(transaccion, cliente)
            archivoHtml.write(
                f"""
                    <li class="list-group-item">
                    <div class="row">
                        <div class="col-md-2">
                            <p>{transaccion["fecha"]}</p>
                            </div>
                            <div class="col-md-2">
                            <p>{transaccion["tipo"]}</p>
                            </div>
                            <div class="col-md-2">
                            <p>{transaccion["estado"]}</p>
                            </div>
                            <div class="col-md-2">
                            <p>{transaccion["monto"]}</p>
                            </div>
                """
            )
            if razon.getRazon() != "OK":
                archivoHtml.write(
                    f"""
                        <div class="col-md-2">
                        <p>{razon.getRazon()}</p>
                        </div>
                    """
                )
        archivoHtml.write("</div></ul>")
    archivoHtml.write("</body>")
    print("Se genero el archivo transaccion.html")
    archivoHtml.close()


if __name__ == "__main__":
    print("Iniciando segmentacion de clientes")
    clientes = generarClientes(*ARCHIVOS)
    print("Se generaron los clientes")
    archivoHtml = crearHTML()
