from Declarations import *

def to_pilaOp(var, line, p):
	line = p.lineno(0)
	var = p[-1]
	if type(var) is int:
		#print var, "is int in line %s" %(line)
		pilaOp.push(var)
		pTypes.push('int')
	elif type(var) is float:
		#print var, "is double in line %s" %(line)
		pilaOp.push(var)
		pTypes.push('double')
	elif var == "true" or p[-1] == "false":
		#print var, "is bool in line %s" %(line)
		pilaOp.push(var)
		pTypes.push('bool')
	elif var in dirProcedures:
		#print var, "is function of type %s in line %s" % (dirProcedures[var]['func_type'], line)
		pilaOp.push(var)
		pTypes.push(dirProcedures[var]['func_type'])
	elif var in varTable[scope[len(scope)-1]]:
		#print p[-1], "is %s in line %s" %(varTable[scope[len(scope)-1]][p[-1]], line)
		pilaOp.push(var)
		pTypes.push(varTable[scope[len(scope)-1]][p[-1]])
	elif var in varTable['global']:
		#print p[-1], "is %s in line %s" %(varTable['global'][p[-1]], line)
		pilaOp.push(var)
		pTypes.push(varTable['global'][p[-1]])
	else:
		print p[-1], 'in line %s is not declared' % line
		#sys.exit()

def gen_est_quad(line, qtype):
	if qtype == 'read':
		print 1
	elif qtype == 'write':
		print 2
	elif qtype == 'cicle':
		print 3
	elif qtype == 'condition':
		print 4
	elif qtype == 'assignation':
		print 5
	elif qtype == 'func_call':
		print 6
	else:
		print 'Cant generate estatement quadruple in line %s' % line
		sys.exit()

def gen_exp_quad(line, qtype):
	optype = None
	if qtype == 'factor':
		optype = mults
	elif qtype == 'term':
		optype = sums
	elif qtype == 'comp':
		optype = comps
	elif qtype == 'conc':
		optype = ands
	else:
		print 'Cant generate expression quadruple in line %s' % line
		sys.exit()

	if pilaOptr.isEmpty():
		return
	elif pilaOptr.peek() in optype and pilaOptr.size() > 1:
		rOperand = pilaOp.peek()
		pilaOp.pop()
		rType = pTypes.peek()
		pTypes.pop()
		lOperand = pilaOp.peek()
		pilaOp.pop()
		lType = pTypes.peek()
		pTypes.pop()
		oper = pilaOptr.peek()
		pilaOptr.pop()
		res = getType(lType, rType, oper)
		if res != 'ERROR':
			global iTempCount
			temp = "t" + str(iTempCount)
			iTempCount += 1 
			quad = Quadruple(oper, lOperand, rOperand, temp)
			quadruples.addQuad(quad)
			pTypes.push(res)
			pilaOp.push(temp)
		else:
			print "Type mismatch in line %s" % line
	'''else:
		print "Not enough operands in stack"
		sys.exit()'''



# ===========================================================================

# Obtener el tipo de la operacion realizada
def getType(ltype, rtype, oper):
	return semanticCube[ltype][rtype][oper]

# Probar que este declarado correctamente el cubo semantico
def printSemanticCube():
	for key in semanticCube:
		for  key2 in semanticCube[key]:
			print semanticCube[key][key2]

# Hacer print de un stack
def printStack(stack):
    print "-------------------"
    while not stack.isEmpty():
        print stack.peek(), ",",
        stack.pop()
    print "\n-------------------"

# Obtener el codigo de operacion
def getOperationCode(oper):
	return operationCodes[oper]

# Probar que este declarado correctamente el diccionario de operaciones
def printOperationCodes():
	for key in operationCodes:
		print operationCodes[key]

# DEsplegar las variables por motivos de debugging
def printAll():
	print "===Var Table==="
	pprint.pprint(varTable)
	print "===Dir Proc==="
	pprint.pprint(dirProcedures)
	print "===Pila Operadores==="
	print 'size', pilaOptr.size()
	printStack(pilaOptr)
	print "===Pila Operandos==="
	print 'size', pilaOp.size()
	printStack(pilaOp)
	print "===Pila Tipos==="
	print 'size', pTypes.size()
	printStack(pTypes)
	print "===Cuadruplos==="
	print 'size', quadruples.size()
	quadruples.printQuadruples()