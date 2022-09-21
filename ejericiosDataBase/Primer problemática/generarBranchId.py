import math
import os
from random import random

DIRECCION_ARCHIVO = os.path.join(os.path.dirname(os.path.realpath(__file__)), "sucursales.sql")


def generarTiposCuenta(direccion_archivo):
    with open(direccion_archivo, "w") as archivo:
        for i in range(1, 105):
            archivo.write(f"UPDATE `prestamo` SET `branch_id` = {math.floor(random() * 50)} WHERE `loan_id` = {i};\n")


if __name__ == "__main__":
    generarTiposCuenta(DIRECCION_ARCHIVO)
