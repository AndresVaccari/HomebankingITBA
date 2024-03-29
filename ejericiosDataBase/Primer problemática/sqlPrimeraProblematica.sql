DROP TABLE tiposCliente

/*Crear en la base de datos los tipos de cliente, de cuenta y marcas de
tarjeta. Insertar los valores según la información provista en el Sprint
5*/
CREATE TABLE tiposCliente (
	 tipoID INTEGER PRIMARY KEY,
	 cantidadMaxChequeras INTEGER NOT NULL,
	 cantidadMaxTarjetas INTEGER NOT NULL,
	 puedeCrearChequera INTEGER NOT NULL CHECK (puedeCrearChequera IN (0,1)),
	 puedeCrearTarjetaCredito INTEGER NOT NULL CHECK (puedeCrearTarjetaCredito IN (0,1)),
	 puedeComprarDolar INTEGER NOT NULL CHECK (puedeComprarDolar IN (0,1))
)

ALTER TABLE cuenta
ADD limiteExtraccionDiario FLOAT;

ALTER TABLE cuenta
ADD limiteTransferenciaRecibida FLOAT;

ALTER TABLE cuenta
ADD costorTransferenciaRecibida FLOAT;

ALTER TABLE cuenta
ADD saldoDescubiertoDisponible FLOAT;

CREATE TABLE marcasTarjeta (
	 marcaID INTEGER PRIMARY KEY,
	 nombreMarca TEXT NOT NULL
)

INSERT INTO marcasTarjeta (nombreMarca)
VALUES
	('Visa'),
	('MasterCard'),
	('AmericanExpress'),
	('Cabal');
	
INSERT INTO tipoTarjeta (nombreTipo)
VALUES
	('Debito'),
	('Credito');

/*Agregar la entidad tarjeta*/
CREATE TABLE tarjeta (
	 tarjetaID INTEGER PRIMARY KEY,
	 marcaID INTEGER NOT NULL,
	 numeroTarjeta TEXT NOT NULL CHECK (length(numeroTarjeta) = 20),
	 CVV TEXT NOT NULL,
	 fechaOtorgamiento DATE NOT NULL,
	 fechaExpiracion DATE NOT NULL,
	 tipoTarjetaID INT NOT NULL,
	 FOREIGN KEY (tipoTarjetaID)
	 REFERENCES tipoTarjeta(tipoTarjetaID),
	 FOREIGN KEY (marcaID)
	 REFERENCES marcasTarjeta(marcaID) /*Relacionar las tarjetas con la tabla donde se guardan las marcas de
tarjeta*/
);

ALTER TABLE tarjeta
ADD customer_id INTEGER NOT NULL;

/*Relacionar las tarjetas con el cliente al que pertenecen*/
ALTER TABLE tarjeta
ADD FOREIGN KEY (customer_id)
REFERENCES cliente(customer_id);

CREATE TABLE tipoTarjeta (
	 tipoTarjetaID INTEGER PRIMARY KEY,
	 nombreTipo TEXT NOT NULL
)

/*Agregar la entidad direcciones*/
CREATE TABLE direcciones (
	idDireccion INT PRIMARY KEY,
	calle TEXT NOT NULL,
	numero TEXT NOT NULL,
	ciudad TEXT NOT NULL,
	provincia TEXT NOT NULL,
	pais TEXT NOT NULL,
	idDirecciones INT NOT NULL,
	FOREIGN KEY (idDirecciones)
	REFERENCES sujetoDireccion(idDirecciones)
)

CREATE TABLE sujetoDireccion (
	idDirecciones INT PRIMARY KEY
)

/*Ampliar el alcance de la entidad cuenta para que identifique el tipo de
la misma*/
ALTER TABLE cuenta
ADD tipoCuenta TEXT;

/*Corregir el campo employee_hire_date de la tabla empleado con la
fecha en formato YYYY-MM-DD*/
SELECT 
	FORMAT (employee_hire_date, 'dd-MM-yy') as date
FROM empleado

UPDATE empleado
SET employee_hire_date = substr(employee_hire_date,7,4)||'-'||substr(employee_hire_date,4,2)||'-'||substr(employee_hire_date,1,2)

UPDATE tarjeta
SET fechaOtorgamiento = substr(fechaOtorgamiento,7,4)||'-'||substr(fechaOtorgamiento,4,2)||'-'||substr(fechaOtorgamiento,1,2),

UPDATE tarjeta
SET fechaExpiracion = substr(fechaExpiracion,7,4)||'-'||substr(fechaExpiracion,4,2)||'-'||substr(fechaExpiracion,1,2);


