import math
import os
from random import random

DIRECCION_ARCHIVO = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tiposCliente.sql")
TIPOS_CLIENTE = [1, 2, 3]


def generarTiposCuenta(direccion_archivo):
    with open(direccion_archivo, "w") as archivo:
        for i in range(1, 501):
            archivo.write(
                f"UPDATE `cliente` SET `tipoCliente` = {TIPOS_CLIENTE[math.floor(random() * 3)]} WHERE `customer_id` = {i};\n"
            )


if __name__ == "__main__":
    generarTiposCuenta(DIRECCION_ARCHIVO)
