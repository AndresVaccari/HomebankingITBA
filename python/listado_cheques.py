from cmath import exp
import sys
import csv
from datetime import datetime

POSICION_ARGUMENTO_NOMBRE_ARCHIVO = 1
POSICION_ARGUMENTO_DNI = 2
POSICION_ARGUMENTO_SALIDA = 3
POSICION_ARGUMENTO_TIPO_CHEQUE = 4
POSICION_ARGUMENTO_RANGO_FECHA = 5

ETIQUETA_CABEVERA_CSV_NUM_CHEQUE = "NroCheque"
ETIQUETA_CABEVERA_CSV_COD_BANCO = "CodigoBanco"
ETIQUETA_CABEVERA_CSV_COD_SUCURSAL = "CodigoSucursal"
ETIQUETA_CABEVERA_CSV_CUENTA_ORIGEN = "NroCuentaOrigen"
ETIQUETA_CABEVERA_CSV_CUENTA_DESTINO = "NroCuentaDestino"
ETIQUETA_CABEVERA_CSV_VALOR = "Valor"
ETIQUETA_CABEVERA_CSV_FECHA_ORIGEN = "FechaOrigen"
ETIQUETA_CABEVERA_CSV_FECHA_PAGO = "FechaPago"
ETIQUETA_CABEVERA_CSV_DNI = "DNI"
ETIQUETA_CABEVERA_CSV_ESTADO = "Estado"


# Definición de errores propios
class Error(Exception):
    """Base class for other exceptions"""

    pass


class ErrorFechaInput(Error):
    """Fecha de input no valida"""

    pass


class ErrorNumeroDeChequeRepetido(Error):
    """Numero de cheque repetido"""

    pass


# Función de comparación de fechas
def comparar_fechas(fecha_inicio, fecha_fin, fecha_pago):
    fechadate_pago = datetime.strptime(fecha_pago, "%d-%m-%Y")
    valido = fecha_inicio <= fechadate_pago <= fecha_fin
    return valido


# Función de entrada, chequeo e ingreso de datos de cheque del cliente
def generar_datos_cliente(posicion_dni, posicion_estado, fecha_inicio,
                          fecha_fin, datos):
    try:
        if sys.argv[POSICION_ARGUMENTO_TIPO_CHEQUE] != "Todos":
            if fecha_inicio == "" or fecha_fin == "":
                datos_cliente = list(
                    filter(
                        lambda registro: (registro[posicion_dni] == sys.argv[
                            POSICION_ARGUMENTO_DNI])
                        & (registro[posicion_estado] == sys.argv[
                            POSICION_ARGUMENTO_TIPO_CHEQUE]),
                        datos,
                    ))
                return datos_cliente
            else:
                if fecha_inicio > fecha_fin:
                    raise ErrorFechaInput
                else:
                    datos_cliente = list(
                        filter(
                            lambda registro: (registro[posicion_dni] == sys.
                                              argv[POSICION_ARGUMENTO_DNI])
                            & (registro[posicion_estado] == sys.argv[
                                POSICION_ARGUMENTO_TIPO_CHEQUE])
                            & comparar_fechas(fecha_inicio, fecha_fin,
                                              registro[posicion_fecha_pago]),
                            datos,
                        ))
                    return datos_cliente
        else:
            if fecha_inicio == "" or fecha_fin == "":
                datos_cliente = list(
                    filter(
                        lambda registro: registro[posicion_dni] == sys.argv[
                            POSICION_ARGUMENTO_DNI],
                        datos,
                    ))
                return datos_cliente
            else:
                if fecha_inicio > fecha_fin:
                    raise ErrorFechaInput
                else:
                    datos_cliente = list(
                        filter(
                            lambda registro: (registro[posicion_dni] == sys.
                                              argv[POSICION_ARGUMENTO_DNI])
                            & comparar_fechas(fecha_inicio, fecha_fin,
                                              registro[posicion_fecha_pago]),
                            datos,
                        ))
                    return datos_cliente
    except ErrorFechaInput:
        print("Fecha de input no valida")
        sys.exit(1)


# Función de obtención de fechas segun rango
def obtener_fechas(rango_fecha):
    if rango_fecha != "":
        fechas = rango_fecha.split(":")
        fechasDate = []
        for fecha in fechas:
            fechasDate.append(datetime.strptime(fecha, "%d-%m-%Y"))
    else:
        fechasDate = ["", ""]
    return fechasDate


# Función de salida, se muestran los datos del cheque solicitado al cliente
def salida(salida, cabecera, datos_cliente, posicion_numero):
    try:
        contadorCheques = []
        for dato in datos_cliente:
            if dato[posicion_numero] not in contadorCheques:
                contadorCheques.append(dato[posicion_numero])
            else:
                raise ErrorNumeroDeChequeRepetido
        if salida == "PANTALLA":
            print(",".join(cabecera))

            for dato in datos_cliente:
                print(",".join(dato))
        elif salida == "CSV":
            with open(
                    f"{sys.argv[POSICION_ARGUMENTO_DNI]}{sys.argv[POSICION_ARGUMENTO_RANGO_FECHA]}.csv",
                    "w",
                    newline="",
            ) as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(cabecera)
                for dato in datos_cliente:
                    writer.writerow(dato)
        else:
            print("Error: Salida no valida")
    except ErrorNumeroDeChequeRepetido:
        print("Error: Numero de cheque repetido")
        sys.exit(1)


def obtener_archivo(nombre_archivo):
    try:
        with open(nombre_archivo) as archivo:
            lector = csv.reader(archivo)
            datos = list(lector)
            return datos
    except FileNotFoundError:
        print("Error: Archivo no encontrado")
        sys.exit(1)


if __name__ == "__main__":
    datos = obtener_archivo(sys.argv[POSICION_ARGUMENTO_NOMBRE_ARCHIVO])

    cabecera = datos[0]

    (
        posicion_numero,
        posicion_cod_banco,
        posicion_cod_sucursal,
        posicion_cuenta_origen,
        posicion_cuenta_destino,
        posicion_valor,
        posicion_fecha_origen,
        posicion_fecha_pago,
        posicion_dni,
        posicion_estado,
    ) = (
        cabecera.index(ETIQUETA_CABEVERA_CSV_NUM_CHEQUE),
        cabecera.index(ETIQUETA_CABEVERA_CSV_COD_BANCO),
        cabecera.index(ETIQUETA_CABEVERA_CSV_COD_SUCURSAL),
        cabecera.index(ETIQUETA_CABEVERA_CSV_CUENTA_ORIGEN),
        cabecera.index(ETIQUETA_CABEVERA_CSV_CUENTA_DESTINO),
        cabecera.index(ETIQUETA_CABEVERA_CSV_VALOR),
        cabecera.index(ETIQUETA_CABEVERA_CSV_FECHA_ORIGEN),
        cabecera.index(ETIQUETA_CABEVERA_CSV_FECHA_PAGO),
        cabecera.index(ETIQUETA_CABEVERA_CSV_DNI),
        cabecera.index(ETIQUETA_CABEVERA_CSV_ESTADO),
    )

    fechas = obtener_fechas(sys.argv[POSICION_ARGUMENTO_RANGO_FECHA])

    datos_cliente = generar_datos_cliente(posicion_dni, posicion_estado,
                                          fechas[0], fechas[1], datos[1:])

    salida(sys.argv[POSICION_ARGUMENTO_SALIDA], cabecera, datos_cliente,
           posicion_numero)
