-- Selección de cuentas con saldo negativo
SELECT *
FROM cuenta
WHERE cuenta.balance < 0

-- Seleccionar el nombre, apellido y edad de los clientes que tengan en el apellido la letra Z
SELECT Nombre, Apellido, Edad
FROM vCliente
WHERE Apellido LIKE '%z%'

-- Seleccionar el nombre, apellido, edad y nombre de sucursal de las personas con nombre “Brendan” y ordenar el resultado por nombre de sucursal
SELECT Nombre, Apellido, Edad, sucursal.branch_name as 'Nombre Sucursal'
FROM vCliente
INNER JOIN sucursal ON SucursalID = sucursal.branch_id
WHERE Nombre LIKE 'Brendan' 
ORDER BY sucursal.branch_name

-- Seleccionar de tabla de préstamos los préstamos con un importe mayor a $80.000 y los préstamos prendarios
SELECT *
FROM prestamo p1
INNER JOIN prestamo p2 ON p1.loan_type = 'PRENDARIO'
WHERE p1.loan_total > 8000000

-- Seleccionar los prestamos con importe mayor que el importe medio de todos los prestamos
SELECT *
FROM prestamo p
WHERE p.loan_total > (
    SELECT avg(loan_total)
    FROM prestamo
)

-- Contar la cantidad de clientes menores a 50 años
SELECT COUNT(Edad) as 'Cantidad de Clientes'
FROM vCliente
WHERE Edad < 50

-- Seleccionar las primeras 5 cuentas con saldo mayor a 8.000$
SELECT *
FROM cuenta
WHERE cuenta.balance > 800000
LIMIT 5

-- Seleccionar los préstamos que tengan fecha en abril, junio y agosto, ordenados por importe
SELECT *
FROM prestamo p
WHERE p.loan_date LIKE '%-04-%' OR p.loan_date LIKE '%-06-%' or p.loan_date LIKE '%-08-%'
ORDER BY p.loan_total

-- Obtener la suma total de los prestamos agrupados por tipo de préstamos
SELECT prestamo.loan_type, SUM(prestamo.loan_total) as loan_total_accu
FROM prestamo
GROUP BY prestamo.loan_type