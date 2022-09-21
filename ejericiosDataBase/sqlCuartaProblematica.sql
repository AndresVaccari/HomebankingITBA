-- Listar la cantidad de clientes por nombre de sucursal de mayor a menor
SELECT sucursal.branch_name as 'Sucursal', COUNT(cliente.customer_id) as 'Cantidad Clientes'
FROM cliente
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
GROUP BY sucursal.branch_name

-- Obtener la cantidad de empleados por cliente por sucursal en un número real
SELECT idBranch, qEmpleados, qClientes, round((qEmpleados*1.0/qClientes*1.0), 2) as 'qEmpleados/qClientes'
FROM (
	SELECT sucursal.branch_id as idBranch, count(cliente.customer_id) as qClientes, qEmpleados
	FROM sucursal
	LEFT JOIN cliente
	ON sucursal.branch_id = cliente.branch_id
	LEFT JOIN (
		SELECT sucursal.branch_id as sucursalID, count(empleado.employee_id) as qEmpleados
		FROM sucursal
		LEFT JOIN empleado
		ON sucursal.branch_id = empleado.branch_id
		GROUP BY sucursal.branch_id
	) as cantidad_Empleados
	ON sucursal.branch_id = cantidad_Empleados.sucursalID
	GROUP BY sucursal.branch_id
) as Division

-- Obtener la cantidad de tarjetas de crédito por tipo por sucursal
SELECT COUNT(tarjeta.numeroTarjeta) as 'Cantidad Tarjetas Credito', sucursal.branch_name as 'Sucursal'
FROM tarjeta
INNER JOIN cliente ON tarjeta.customer_id = cliente.customer_id
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
WHERE tarjeta.tipoTarjetaID = 2
GROUP BY sucursal.branch_name

-- Obtener el promedio de créditos otorgado por sucursal
SELECT avg(prestamo.loan_total) as 'Promedio Prestamo', sucursal.branch_name as 'Sucursal'
FROM prestamo
INNER JOIN cliente ON prestamo.customer_id = cliente.customer_id
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
GROUP BY sucursal.branch_name

-- Crear una tabla denominada “auditoria_cuenta” para guardar los datos movimientos
CREATE TABLE auditoria_cuenta (
	old_id INTEGER PRIMARY KEY,
	new_id INTEGER NOT NULL,
	old_balance INTEGER NOT NULL,
	new_balance INTEGER NOT NULL,
	old_iban INTEGER NOT NULL,
	new_iban INTEGER NOT NULL,
	old_type INTEGER NOT NULL,
	new_type INTEGER NOT NULL,
	user_action TEXT NOT NULL,
	created_at TEXT NOT NULL
)

-- Crear un trigger que después de actualizar en la tabla cuentas los campos balance, IBAN o tipo de cuenta registre en la tabla auditoria
CREATE TRIGGER actualizarCuenta
AFTER UPDATE OF balance, iban, tipoCuenta ON cuenta
BEGIN
	INSERT INTO auditoria_cuenta (old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type, new_type, user_action, created_at)
	VALUES (OLD.account_id, NEW.account_id, OLD.balance, NEW.balance, OLD.iban, NEW.iban, OLD.tipoCuenta, NEW.tipoCuenta, 'Actualizar Cuenta', CURRENT_TIMESTAMP);
END

DROP TRIGGER IF EXISTS actualizarCuenta

DELETE FROM auditoria_cuenta

-- Restar $100 a las cuentas 10,11,12,13,14
UPDATE cuenta
SET balance = balance - 10000
WHERE account_id BETWEEN 10 AND 14

-- Mediante índices mejorar la performance la búsqueda de clientes por DNI
CREATE UNIQUE INDEX idx_cuenta_dni 
ON cliente (customer_DNI)

-- Crear la tabla “movimientos” con los campos de identificación del movimiento, número de cuenta, monto, tipo de operación y hora
CREATE TABLE movimientos (
	movimientoID INTEGER PRIMARY KEY,
	account_id INTEGER NOT NULL,
	monto INTEGER NOT NULL,
	tipoMovimiento TEXT NOT NULL,
	created_at TEXT NOT NULL
)

-- Hacer una transferencia de 1000$desde la cuenta 200 a la cuenta 400
BEGIN TRANSACTION;

UPDATE cuenta
SET balance = balance - 100000
WHERE account_id = 200;

UPDATE cuenta
SET balance = balance + 100000
WHERE account_id = 400;

-- Registrar el movimiento en la tabla movimientos
INSERT INTO movimientos (account_id, monto, tipoMovimiento, created_at)
VALUES
	(200, -100000, 'Envio_Dinero', CURRENT_TIMESTAMP),
	(400, 100000, 'Recibo_Dinero', CURRENT_TIMESTAMP);

COMMIT;