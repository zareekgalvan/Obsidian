from Declarations import *

# SEMANTIC AND SINTAX VALIDATION FUNCTIONS
# ===========================================================================
def check_arr_param(p):
	line = p.lineno(0)
	if len(p) > 1 and type(p[2]) is not int:
		print 'Type mismatch in line %s with value %s' % (line, p[2])
		sys.exit()

def to_var_table(p):
	varid = p[-2]
	line = p.lineno(0)
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  lastType[len(lastType)-1]
	else:
		print('Variable "%s" in line %s already registered' % (varid, line))
		sys.exit()

def to_proc_dir(p):
	procname = p[-1]
	functype = p[-2]
	line = p.lineno(0)
	if procname not in scope and procname not in varTable['global']:
		scope.append(procname)
		varTable['global'][procname] = functype
		varTable[procname] = {}
		dirProcedures[procname] = {}
		dirProcedures[procname]['func_type'] = functype
		dirProcedures[procname]['args'] = []
	else:
		print('Function "%s" already registered in line %s' % (procname, line))
		sys.exit()

def to_args(varid, vartype, line, p):
	dirProcedures[scope[len(scope)-1]]['args'].append(p[-2])
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  vartype
	else:
		print('Variable "%s" in line %s already registered' % (varid, line))
		sys.exit() 

def actual_quad_no(scope):
	dirProcedures[scope]['params_no'] = len(dirProcedures[scope]['args'])
	dirProcedures[scope]['vars_no'] = len(varTable[scope]) - dirProcedures[scope]['params_no']
	dirProcedures[scope]['quad_start'] = Quadruples.cont

def is_valid_func(p):
	varid = p[-1]
	line = p.lineno(0)
	if varid not in dirProcedures:
		print '%s in line %s is not a valid function' % (varid, line)
		#sys.exit()

# QUAD GENERATION FUNCTIONS
# ===========================================================================
def pop_false_bottom():
	if pilaOptr.peek() == '(':
		pilaOptr.pop()
	else:
		print "No es un '(' al top de la pilaOptr"
		sys.exit()

def to_pilaOp(var, line, p):
	if type(var) is int:
		print var, "is int in line %s" %(line)
		pilaOp.push(var)
		pTypes.push('int')
	elif type(var) is float:
		print var, "is double in line %s" %(line)
		pilaOp.push(var)
		pTypes.push('double')
	elif var == "true" or var == "false":
		print var, "is bool in line %s" %(line)
		pilaOp.push(var)
		pTypes.push('bool')
	elif var in dirProcedures and var in varTable['global']:
		print var, "is function of type %s in line %s" % (dirProcedures[var]['func_type'], line)
		pass
		pilaOp.push(var)
		pTypes.push(dirProcedures[var]['func_type'])
	elif var in varTable[scope[len(scope)-1]]:
		print var, "is %s in line %s" %(varTable[scope[len(scope)-1]][var], line)
		pilaOp.push(var)
		pTypes.push(varTable[scope[len(scope)-1]][var])
	elif var in varTable['global']:
		print var, "is %s in line %s" %(varTable['global'][var], line)
		pilaOp.push(var)
		pTypes.push(varTable['global'][var])
	else:
		print var, 'in line %s is not declared' % line
		#sys.exit()

def check_type(p):
	line = p.lineno(0)
	exp = pilaOp.peek()
	expType = pTypes.peek()
	if expType == 'bool':
		res = pilaOp.peek()
		pilaOp.pop()
		pTypes.pop()
		gen_gotof_quad(res)
	else:
		print "Type mismatch in line %s with val %s" % (line, expType)
		sys.exit()

def gen_est_quad(line, qtype):
	if qtype == 'read':
		gen_read_quad(line)
	elif qtype == 'write':
		gen_write_quad(line)
	elif qtype == 'assignation':
		gen_assignation_quad(line)
	elif qtype == 'func_call':
		print 6
	elif qtype == 'declaration_assign':
		gen_declaration_assign_quad(line)
	else:
		print 'Cant generate estatement quadruple in line %s' % line
		sys.exit()

def gen_declaration_assign_quad(line):
	if pilaOp.size() > 1:
		oper = pilaOp.peek()
		pilaOp.pop()
		operType = pTypes.peek()
		pTypes.pop()
		temp = pilaOp.peek()
		pilaOp.pop()
		tempType = pTypes.peek()
		pTypes.pop()
		if getType(operType, tempType, '=') != 'ERROR':
			quad = Quadruple(Quadruples.cont, '=', oper, '', temp)
			quadruples.addQuad(quad)
		else:
			print "Type mismatch in line %s" % line
			sys.exit()
	else:
		print 'Cant generate declaration assignation estatement quadruple in line %s' % line

def gen_read_quad(line):
	if pilaOp.size() > 0:
		temp = pilaOp.peek()
		pilaOp.pop()
		pTypes.pop()
		quad = Quadruple(Quadruples.cont, 'read', '', '', temp)
		quadruples.addQuad(quad)
	else:
		print 'Cant generate read estatement quadruple in line %s' % line

def gen_write_quad(line):
	if pilaOp.size() > 0:
		temp = pilaOp.peek()
		pilaOp.pop()
		pTypes.pop()
		quad = Quadruple(Quadruples.cont, 'write', '', '', temp)
		quadruples.addQuad(quad)
	else:
		print 'Cant generate write estatement quadruple in line %s' % line

def var_assign(p):
	if len(p) > 1:
		line = p.lineno(0)
		var = p[-3]
		to_pilaOp(var, line, p)
		var = p[2]
		to_pilaOp(var, line, p)
		line = p.lineno(0)
		gen_est_quad(line, 'declaration_assign')

def gen_assignation_quad(line):
	if pilaOp.size() > 1:
		oper = pilaOp.peek()
		pilaOp.pop()
		operType = pTypes.peek()
		pTypes.pop()
		temp = pilaOp.peek()
		pilaOp.pop()
		tempType = pTypes.peek()
		pTypes.pop()
		if getType(operType, tempType, '=') != 'ERROR':
			quad = Quadruple(Quadruples.cont, '=', oper, '', temp)
			quadruples.addQuad(quad)
		else:
			print "Type mismatch in line %s" % line
			sys.exit()
	else:
		print 'Cant generate assignation estatement quadruple in line %s' % line

def gen_gotof_quad(res):
	quad = Quadruple(Quadruples.cont, 'GotoF', res, '', '')
	quadruples.addQuad(quad)
	pSaltos.push(Quadruples.cont-1)

def gen_goto():
	false = pSaltos.peek()
	pSaltos.pop()
	pSaltos.push(Quadruples.cont-1)
	quadruples.fillQuad(false, Quadruples.cont)

def fill_end_condition():
	end = pSaltos.peek()
	pSaltos.pop()
	quadruples.fillQuad(end, Quadruples.cont)

def cycle_start():
	pSaltos.push(Quadruples.cont)

def cycle_end():
	end = pSaltos.peek()
	pSaltos.pop()
	ret = pSaltos.peek()
	pSaltos.pop()
	quad = Quadruple(Quadruples.cont, 'Goto', '', '', ret)
	quadruples.addQuad(quad)
	quadruples.fillQuad(end, Quadruples.cont)

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
	elif pilaOptr.peek() in optype and pilaOptr.size() >= 1:
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
			quad = Quadruple(Quadruples.cont, oper, lOperand, rOperand, temp)
			quadruples.addQuad(quad)
			pTypes.push(res)
			pilaOp.push(temp)
		else:
			print "Type mismatch in line %s" % line
			sys.exit()
	#else:
	#	print "Not enough operands in stack in line %s" % line
		#sys.exit()

def gen_return_quad(scope, p):
	line = p.lineno(0)
	ret = pilaOp.peek()
	pilaOp.pop()
	retType = pTypes.peek()
	pTypes.pop()
	functype = dirProcedures[scope]['func_type']
	if functype == retType:
		quad = Quadruple(Quadruples.cont, 'return', '', '',ret)
		quadruples.addQuad(quad)
	else:
		print "Type mismatch of return in line %s" % line
		sys.exit()

def gen_endproc_quad(p):
	lastscope =scope[len(scope)-1]
	if lastscope != 'void' and p[-1] == None:
		print "Invalid syntax, function %s has no return" % lastscope
		sys.exit()
	quad = Quadruple(Quadruples.cont, 'EndP', '', '','')
	quadruples.addQuad(quad)

def gen_end_quad():
	quad = Quadruple(Quadruples.cont, 'END', '', '','')
	quadruples.addQuad(quad)

# OTHER FUNCTIONS
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
	print "===\t\tVar Table\t\t==="
	pprint.pprint(varTable)
	print "===\t\tDir Proc\t\t==="
	pprint.pprint(dirProcedures)
	print "===\t\tPila Operadores\t\t==="
	print 'size', pilaOptr.size()
	printStack(pilaOptr)
	print "===\t\tPila Operandos\t\t==="
	print 'size', pilaOp.size()
	printStack(pilaOp)
	print "===\t\tPila Tipos\t\t==="
	print 'size', pTypes.size()
	printStack(pTypes)
	print "===\t\tPila Saltos\t\t==="
	print 'size', pSaltos.size()
	printStack(pSaltos)
	print "===\t\tCuadruplos\t\t==="
	print 'size', quadruples.size()
	quadruples.printQuadruples()