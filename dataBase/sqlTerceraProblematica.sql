SELECT *
FROM cuenta
WHERE cuenta.balance < 0

SELECT Nombre, Apellido, Edad
FROM vCliente
WHERE Apellido LIKE '%z%'

SELECT Nombre, Apellido, Edad, sucursal.branch_name as 'Nombre Sucursal'
FROM vCliente
INNER JOIN sucursal ON SucursalID = sucursal.branch_id

SELECT *
FROM prestamo p1
INNER JOIN prestamo p2 ON p1.loan_type = 'PRENDARIO'
WHERE p1.loan_total > 8000000

SELECT *
FROM prestamo p
WHERE p.loan_total > (
    SELECT avg(loan_total)
    FROM prestamo
)

SELECT COUNT(Edad) as 'Cantidad de Clientes'
FROM vCliente
WHERE Edad < 50

SELECT *
FROM cuenta
WHERE cuenta.balance > 800000
LIMIT 5

SELECT *
FROM prestamo p
WHERE p.loan_date LIKE '%-04-%' OR p.loan_date LIKE '%-06-%' or p.loan_date LIKE '%-08-%'
ORDER BY p.loan_total

SELECT prestamo.loan_type, SUM(prestamo.loan_total) as loan_total_accu
FROM prestamo
GROUP BY prestamo.loan_type