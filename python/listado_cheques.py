import sys
import csv

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


def generar_datos_cliente(posicion_dni, posicion_estado, tipo_estado, fecha_inicio, fecha_fin):
    datos_cliente = list(filter(
        lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] & registro[posicion_estado] == tipo_estado, datos[1:]))
    return datos_cliente


def busqueda_por_tipo_cheque(tipo_cheque):
    if tipo_cheque == 'Pendiente':
        datos_cliente = list(filter(
            lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] & registro[posicion_estado] == 'Pendiente', datos[1:]))
    elif tipo_cheque == 'Aprobado':
        datos_cliente = list(filter(
            lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] & registro[posicion_estado] == 'Aprobado', datos[1:]))
    elif tipo_cheque == 'Rechazado':
        datos_cliente = list(filter(
            lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] & registro[posicion_estado] == 'Rechazado', datos[1:]))
    return datos_cliente


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

    if sys.argv[POSICION_ARGUMENTO_TIPO_CHEQUE] != 'Todos':
        datos_cliente = busqueda_por_tipo_cheque(
            sys.argv[POSICION_ARGUMENTO_TIPO_CHEQUE])

    datos_cliente = list(filter(
        lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))

    print(','.join(cabecera))

    for dato in datos_cliente:
        print(','.join(dato))
