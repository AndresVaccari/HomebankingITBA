DROP TABLE tiposCliente

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
	 REFERENCES marcasTarjeta(marcaID)
);

ALTER TABLE tarjeta
ADD customer_id INTEGER NOT NULL;

ALTER TABLE tarjeta
ADD FOREIGN KEY (customer_id)
REFERENCES cliente(customer_id);

CREATE TABLE tipoTarjeta (
	 tipoTarjetaID INTEGER PRIMARY KEY,
	 nombreTipo TEXT NOT NULL
)

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

ALTER TABLE cuenta
ADD tipoCuenta TEXT;

SELECT 
	FORMAT (employee_hire_date, 'dd-MM-yy') as date
FROM empleado


