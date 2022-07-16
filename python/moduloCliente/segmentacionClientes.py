import json
from clienteBlack import ClienteBlack
from clienteClassic import ClienteClassic
from clienteGold import ClienteGold
from razon import Razon

ARCHIVOS = (
    "ejemplosJson/eventos_black.json",
    "ejemplosJson/eventos_classic.json",
    "ejemplosJson/eventos_gold.json",
)


def generarClientes(*args):
    clientes = []
    for direccion in args:
        arch = open(direccion, "r")
        datos = json.load(arch)
        for cliente in datos:
            if cliente["tipo"] == "BLACK":
                clientes.append(ClienteBlack(cliente))
            elif cliente["tipo"] == "GOLD":
                clientes.append(ClienteGold(cliente))
            else:
                clientes.append(ClienteClassic(cliente))
            print("Cliente creado")
    return clientes
    # for direccion in args:
    #     with open(direccion, "r") as archivo:
    #         clientes_json = json.load(archivo)
    #         for cliente in clientes_json:
    #             if cliente["tipo"] == "BLACK":
    #                 clientes.append(ClienteBlack(cliente))
    #             elif cliente["tipo"] == "GOLD":
    #                 clientes.append(ClienteGold(cliente))
    #             else:
    #                 clientes.append(ClienteClassic(cliente))
    #             print("Cliente creado")
    # return clientes


def crearHTML():
    archivoHtml = open("transaccion.html", "w")
    return archivoHtml


if __name__ == "__main__":
    print("Iniciando segmentacion de clientes")
    clientes = generarClientes(*ARCHIVOS)
    print("Se generaron los clientes")
    archivoHtml = crearHTML()
    print("Se creo el archivo HTML")
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
            <body>
        """
    )
    for cliente in clientes:
        print("test1")
        archivoHtml.write(
            f"""
                <h1>{cliente['nombre']} {cliente['apellido']}</h1>
                <h1>{cliente['numero']}</h1>
                <h1>{cliente['dni']}</h1>
                <h1>{cliente['direccion']['calle']} {cliente['direccion']['numero']} ({cliente['direccion']['ciudad']}/{cliente['direccion']['provincia']}/{cliente['direccion']['pais']})</h1>

                <h2>Transacciones</h2>
                <ul class="list-group">
            """
        )
        diccTransacciones = cliente.getTransacciones()
        for transaccion in diccTransacciones:
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
            razon = Razon(transaccion, cliente)
            if razon != "Realizada correctamente":
                archivoHtml.write(
                    f"""<div class="col-md-2">
                        <p>{razon}</p>
                        </div>"""
                )
            archivoHtml.write("</div>")
    archivoHtml.write("""</body>""")
    print("Se genero el archivo transaccion.html")
    archivoHtml.close()
