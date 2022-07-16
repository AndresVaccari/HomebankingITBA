from traceback import print_tb
from cliente import Cliente
from clienteBlack import ClienteBlack
from clienteClassic import ClienteClassic
from clienteGold import ClienteGold
from razon import Razon

dicc = {
    "numero": 100001,
    "nombre": "Nicolas",
    "apellido": "Gaston",
    "dni": "29494777",
    "tipo": "BLACK",
    "direccion": {
        "calle": "Rivadavia",
        "numero": "7900",
        "ciudad": "Capital Federal",
        "provincia": "Buenos Aires",
        "pais": "Argentina",
    },
    "transacciones": [
        {
            "estado": "ACEPTADA",
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 9000,
            "cantidadExtraccionesHechas": 1,
            "monto": 1000,
            "fecha": "06/06/2022 10:00:55",
            "numero": 1,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "RECHAZADA",
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 10000,
            "monto": 11000,
            "fecha": "06/06/2022 10:10:55",
            "numero": 2,
            "saldoEnCuenta": 10000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "RECHAZADA",
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 9000,
            "fecha": "06/06/2022 10:22:55",
            "numero": 3,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "RECHAZADA",
            "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 9000,
            "fecha": "06/06/2022 10:33:33",
            "numero": 4,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "RECHAZADA",
            "tipo": "ALTA_TARJETA_CREDITO",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 9000,
            "fecha": "06/06/2022 12:00:00",
            "numero": 5,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "RECHAZADA",
            "tipo": "ALTA_CHEQUERA",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 9000,
            "fecha": "06/06/2022 12:30:55",
            "numero": 6,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "ACEPTADA",
            "tipo": "COMPRA_DOLAR",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 9000,
            "fecha": "06/06/2022 12:45:33",
            "numero": 7,
            "saldoEnCuenta": 5000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "RECHAZADA",
            "tipo": "TRANSFERENCIA_ENVIADA",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 1000000,
            "fecha": "06/06/2022 13:00:55",
            "numero": 8,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "ACEPTADA",
            "tipo": "TRANSFERENCIA_RECIBIDA",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 9000,
            "fecha": "06/06/2022 13:11:15",
            "numero": 9,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
        {
            "estado": "ACEPTADA",
            "tipo": "TRANSFERENCIA_RECIBIDA",
            "cuentaNumero": 190,
            "cupoDiarioRestante": 3000,
            "monto": 200000,
            "fecha": "06/06/2022 16:00:55",
            "numero": 10,
            "saldoEnCuenta": 100000,
            "totalTarjetasDeCreditoActualmente": 5,
            "totalChequerasActualmente": 2,
        },
    ],
}

if dicc["tipo"] == "BLACK":
    clienteTest = ClienteBlack(dicc)
elif dicc["tipo"] == "GOLD":
    clienteTest = ClienteGold(dicc)
else:
    clienteTest = ClienteClassic(dicc)

diccTransacciones = clienteTest.getTransacciones()

archivoHtml = open("transaccion.html", "w")
archivoHtml.write(f'''<!DOCTYPE html>
<head>
<html lang="en">
<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous" />
</head>
<body>
<h1>{dicc['nombre']} {dicc['apellido']}</h1>
<h1>{dicc['numero']}</h1>
<h1>{dicc['dni']}</h1>
<h1>{dicc['direccion']['calle']} {dicc['direccion']['numero']} ({dicc['direccion']['ciudad']}/{dicc['direccion']['provincia']}/{dicc['direccion']['pais']})</h1>

<h2>Transacciones</h2>
<ul class="list-group">
''')

for transaccion in diccTransacciones:
    archivoHtml.write(f'''<li class="list-group-item">
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
                </div>''')
    razon = Razon(transaccion, clienteTest)
    if (razon != 'Realizada correctamente'):
        archivoHtml.write(f'''<div class="col-md-2">
                <p>{razon}</p>
                </div>''')
    archivoHtml.write('</div>')

archivoHtml.write('''</body>''')
archivoHtml.close()
