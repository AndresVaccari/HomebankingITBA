import os

DIRECCION_ARCHIVO = os.path.join(os.path.dirname(os.path.realpath(__file__)), "idDirecciones.sql")


def generarDirecciones(direccion_archivo):
    with open(direccion_archivo, "w") as archivo:
        for i in range(1, 501):
            archivo.write(f"UPDATE `cliente` set `idDirecciones` = {i} where `customer_id` = {i};\n")
        for i in range(501, 1001):
            archivo.write(f"UPDATE `empleado` set `idDirecciones` = {i} where `employee_id` = {i - 500};\n")
        for i in range(1001, 1101):
            archivo.write(f"UPDATE `sucursal` set `idDirecciones` = {i} where `branch_id` = {i - 1000};\n")


if __name__ == "__main__":
    generarDirecciones(DIRECCION_ARCHIVO)
