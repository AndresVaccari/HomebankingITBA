import os

from moduloSegmentacionCliente.segmentacionClientes import main

# Definicion de los directorios de los archivos de json
ARCHIVOS = (
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosBlack.json"),
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosClassic.json"),
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosGold.json"),
)

if __name__ == "__main__":
    main(ARCHIVOS)
