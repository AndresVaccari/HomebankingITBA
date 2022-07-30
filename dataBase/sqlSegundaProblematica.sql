CREATE VIEW vCliente
AS
SELECT 
    cliente.customer_id as ID,
    cliente.branch_id as SucursalID,
    cliente.customer_name as Nombre, 
    cliente.customer_surname as Apellido,
    cliente.customer_DNI as DNI,
    cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', cliente.dob) as int) as Edad
FROM cliente

DROP VIEW vCliente

SELECT *
FROM vCliente
WHERE Edad > 40
ORDER BY DNI

SELECT *
FROM vCliente
WHERE Nombre LIKE 'Anne' OR Nombre LIKE 'Tyler' 
ORDER BY Edad

INSERT INTO cliente (customer_name, customer_surname, customer_DNI, branch_id, dob)
VALUES
    ('Lois', 'Stout', '47730534', 80, '1984-07-07'),
    ('Hall', 'Mcconnell', '52055464', 45, '1968-04-30'),
    ('Hilel', 'Mclean', '43625213', 77, '1993-03-28'),
    ('Jin', 'Cooley', '21207908', 96, '1959-08-24'),
    ('Gabriel', 'Harmon', '57063950', 27, '1976-04-01')

UPDATE cliente
SET branch_id = 10
WHERE customer_id > 500

DELETE FROM cliente
WHERE cliente.customer_name = 'Noel' AND cliente.customer_surname = 'David'

SELECT prestamo.loan_type as 'Tipo Prestamo', prestamo.loan_total as Valor
FROM prestamo
WHERE Valor = (
	SELECT MAX(prestamo.loan_total)
	FROM prestamo
)