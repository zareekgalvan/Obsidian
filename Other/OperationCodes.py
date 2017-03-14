# Codigos de operacines por simbolos
operationCodes = {
	'+' : 1,
	'-' : 2,
	'*' : 3,
	'/' : 4,
	'%' : 5,
	'=' : 6,
	'==' : 7,
	'!=' : 8,
	'<' : 9,
	'>' : 10,
	'<=' : 11,
	'>=' : 12,
	'&&' : 13,
	'||' : 14,
	'read' : 15,
	'write' : 16,
	'return' : 17
}

# Obtener el codigo de operacion
def getOperationCode(oper):
	return operationCodes[oper]

# Probar que este declarado correctamente el diccionario de operaciones
def printOperationCodes():
	for key in operationCodes:
		print operationCodes[key]