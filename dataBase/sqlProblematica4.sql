SELECT idBranch, qClientes, qEmpleados, round((qClientes*1.0/qEmpleados*1.0), 2) as qClientesDivididoqEmpleados
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

SELECT 
	branch_id as Sucursal, count(customer_id) as Cantidad_Clientes
FROM cliente
GROUP BY branch_id

SELECT 
	branch_id as Sucursal, count(employee_id) as Cantidad_Empleados
FROM empleado
GROUP BY branch_id