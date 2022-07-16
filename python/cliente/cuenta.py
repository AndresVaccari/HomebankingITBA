class Cuenta:
    def __init__(self, dicc):
        print(dict.keys(dicc))


dicc = {"Nombre": "Andres", "Apellido": "Vaccari", "Edad": 21}

Cuenta(dicc)
