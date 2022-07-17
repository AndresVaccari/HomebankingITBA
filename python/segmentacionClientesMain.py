import os

from moduloSegmentacionCliente.segmentacionClientes import main

ARCHIVOS = (
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosBlack.json"),
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosClassic.json"),
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "ejemplosJson\eventosGold.json"),
)

if __name__ == "__main__":
    main(ARCHIVOS)
