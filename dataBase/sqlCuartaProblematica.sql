SELECT sucursal.branch_name as 'Sucursal', COUNT(cliente.customer_id) as 'Cantidad Clientes'
FROM cliente
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
GROUP BY sucursal.branch_name

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

SELECT COUNT(tarjeta.numeroTarjeta) as 'Cantidad Tarjetas Credito', sucursal.branch_name as 'Sucursal'
FROM tarjeta
INNER JOIN cliente ON tarjeta.customer_id = cliente.customer_id
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
WHERE tarjeta.tipoTarjetaID = 2
GROUP BY sucursal.branch_name

SELECT avg(prestamo.loan_total) as 'Promedio Prestamo', sucursal.branch_name as 'Sucursal'
FROM prestamo
INNER JOIN cliente ON prestamo.customer_id = cliente.customer_id
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
GROUP BY sucursal.branch_name

