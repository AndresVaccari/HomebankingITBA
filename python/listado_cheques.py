import sys
import csv
from datetime import datetime

POSICION_ARGUMENTO_NOMBRE_ARCHIVO = 1
POSICION_ARGUMENTO_DNI = 2
POSICION_ARGUMENTO_SALIDA = 3
POSICION_ARGUMENTO_TIPO_CHEQUE = 4
POSICION_ARGUMENTO_RANGO_FECHA = 5

ETIQUETA_CABEVERA_CSV_NUM_CHEQUE = 'NroCheque'
ETIQUETA_CABEVERA_CSV_COD_BANCO = 'CodigoBanco'
ETIQUETA_CABEVERA_CSV_COD_SUCURSAL = 'CodigoSucursal'
ETIQUETA_CABEVERA_CSV_CUENTA_ORIGEN = 'NroCuentaOrigen'
ETIQUETA_CABEVERA_CSV_CUENTA_DESTINO = 'NroCuentaDestino'
ETIQUETA_CABEVERA_CSV_VALOR = 'Valor'
ETIQUETA_CABEVERA_CSV_FECHA_ORIGEN = 'FechaOrigen'
ETIQUETA_CABEVERA_CSV_FECHA_PAGO = 'FechaPago'
ETIQUETA_CABEVERA_CSV_DNI = 'DNI'
ETIQUETA_CABEVERA_CSV_ESTADO = 'Estado'


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ErrorFechaInput(Error):
    """Fecha de input no valida"""
    pass


def generar_datos_cliente(posicion_dni, posicion_estado, fecha_inicio, fecha_fin, datos):
    try:
        if sys.argv[POSICION_ARGUMENTO_TIPO_CHEQUE] != 'Todos':
            if fecha_inicio == '':
                if fecha_inicio > fecha_fin:
                    raise ErrorFechaInput
                else:
                    datos_cliente = list(filter(
                        lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] & registro[posicion_estado] == sys.argv[POSICION_ARGUMENTO_TIPO_CHEQUE], datos[1:]))
                    return datos_cliente
            else:
                datos_cliente = list(filter(
                    lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] & registro[posicion_estado] == sys.argv[POSICION_ARGUMENTO_TIPO_CHEQUE] & registro[posicion_fecha_origen] >= fecha_inicio & registro[posicion_fecha_pago] <= fecha_fin, datos[1:]))
                return datos_cliente
        else:
            if fecha_inicio == '':
                datos_cliente = list(filter(
                    lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))
                return datos_cliente
            else:
                datos_cliente = list(filter(
                    lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] & registro[posicion_fecha_origen] >= fecha_inicio & registro[posicion_fecha_pago] <= fecha_fin, datos[1:]))
                return datos_cliente
    except ErrorFechaInput:
        print('Fecha de input no valida')
        sys.exit(1)


def obtener_fechas(rango_fecha):
    if rango_fecha != '':
        fechas = rango_fecha.split(':')
        fechasDate = []
        for fecha in fechas:
            fechasDate.append(datetime.strptime(fecha, '%Y-%m-%d'))
    else:
        fechasDate = ['', '']
    return fechasDate


if __name__ == '__main__':
    with open(sys.argv[POSICION_ARGUMENTO_NOMBRE_ARCHIVO]) as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)

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
        posicion_estado
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
        cabecera.index(ETIQUETA_CABEVERA_CSV_ESTADO)
    )

    fechas = obtener_fechas(sys.argv[POSICION_ARGUMENTO_RANGO_FECHA])

    datos_cliente = generar_datos_cliente(
        posicion_dni, posicion_estado, fechas[0], fechas[1], datos)

    print(','.join(cabecera))

    for dato in datos_cliente:
        print(','.join(dato))
