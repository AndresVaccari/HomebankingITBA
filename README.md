# Homebanking ITBA

Proyecto hecho realizado en equipo para el curso Full Stack Developer de ITBA utilizando:

- HTML
- CSS
- JavaScript
- Python
- SQLite
- Django
- Boostrap

## Requisitos para el servidor

Requiere tener instalador django y django rest framework

## Usuarios registrados

Ya hay algunos usuarios registrados que se pueden utilizar para navegar por el homebanking, los cuales son:

- leslie1999, pass: 1999moses - Cliente
- moses, pass: greer1234 - Cliente
- conan, pass: livin1234 - Empleado

El usuario de tipo empleado solo es valido a la hora de usar la API

## API

El homebanking cuenta con un API la cual se accede desde /API
Mediante la API se puede acceder a los siguentes datos:

- Obtener datos de un cliente:
  - Se realiza desde /API/cliente
  - Si lo realiza un empleado puede ver la lista de todos los clientes, un cliente solo se puede ver a si mismo
- Obtener saldo de cuenta de un Cliente:
  - Se realiza desde /API/cuenta
  - Si lo realiza un empleado puede ver la lista de todos las cuentas, un cliente solo se puede ver a si mismo
- Obtener monto de prestamo de una sucursal:
  - Se realiza desde /API/totalPrestamos
  - Solo lo puede realizar un empleado
- Obtener tarjetas asociadas a un cliente
  - Se realiza desde /API/tarjetas/{idcliente}
  - No se puede acceder al listado total de las tarjetas, solo al de un cliente en especifico
  - Solo puede realizarlo un empleado
- Generar/Anular una solicitud de prestamo
  - Se realiza desde /API/gestionPrestamos
  - Solo puede realizarlo un empleado
  - Hay que poner un / despues de la pk a la hora de hacer el delete, ejemplo: /API/gestionPrestamos/18/
- Modificar la direccion de un cliente
  - Un realiza desde /API/direcciones
  - Un empleado puede modificar la direccion de cualquier cliente, un cliente solo puede modificar su direccion
  - Con el metodo GET se puede listar las direcciones, igualmente un empleado puede ver todas las direcciones y un cliente solo la suya
- Listado de todas las sucursales
  - Se realiza desde /API/sucursales
  - Puede acceder cualquier persona, este autorizada o no
