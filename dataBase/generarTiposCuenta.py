import math
import os
from random import random

DIRECCION_ARCHIVO = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tiposCuenta.sql")
TIPOS_CUENTA = ["'Caja de Ahorro en Pesos'", "'Caja de Ahorro en Dolares'", "'Cuenta Corriente'"]


def generarTiposCuenta(direccion_archivo):
    with open(direccion_archivo, "w") as archivo:
        for i in range(1, 501):
            archivo.write(
                f"UPDATE `cuenta` SET `tipoCuenta` = {TIPOS_CUENTA[math.floor(random() * 3)]} WHERE `customer_id` = {i};\n"
            )


if __name__ == "__main__":
    generarTiposCuenta(DIRECCION_ARCHIVO)
