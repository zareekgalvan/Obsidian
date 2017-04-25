from Declarations import *
import pprint


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
		varTable[scope[len(scope)-1]][varid] = {}
		varTable[scope[len(scope)-1]][varid]['type'] =  lastType[len(lastType)-1]
		varTable[scope[len(scope)-1]][varid]['address'] = mem.avail(lastType[len(lastType)-1])
	else:
		print 'Variable "%s" in line %s already registered' % (varid, line)
		sys.exit()


def to_proc_dir(p):
	procname = p[-1]
	functype = p[-2]
	line = p.lineno(0)
	if procname not in scope and procname not in varTable['global']:
		scope.append(procname)
		varTable['global'][procname] = {}
		varTable['global'][procname]['type'] = functype
		varTable['global'][procname]['address'] = mem.avail(functype)
		varTable[procname] = {}
		dirProcedures[procname] = {}
		dirProcedures[procname]['func_type'] = functype
		dirProcedures[procname]['args'] = []
	else:
		print 'Function "%s" already registered in line %s' % (procname, line)
		sys.exit()


def to_args(varid, vartype, line, p):
	dirProcedures[scope[len(scope)-1]]['args'].append(vartype)
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  {}
		varTable[scope[len(scope)-1]][varid]['type'] = vartype
		varTable[scope[len(scope)-1]][varid]['address'] = mem.availVar(vartype)
	else:
		print 'Variable "%s" in line %s already registered' % (varid, line)
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


def getConstType(p):
	if type(p) is int:
		return 'int'
	elif type(p) is float:
		return 'double'
	elif p == 'true' or p == 'false':
		return 'bool'


def exitsInVarTable(var):
	if var in varTable[scope[len(scope)-1]]:
		return True
	else:
		return False


def tryRegisterVar(var):
	if var in varTable['constants']:
		return varTable['constants'][var]

	elif var in varTable[scope[len(scope)-1]]:
		return varTable[scope[len(scope)-1]][var]
	elif var in varTable['global']:
		return varTable['global'][var]
	else:
		varTable['constants'][var] = {}
		typee = getConstType(var)
		varTable['constants'][var]['type'] = typee
		varTable['constants'][var]['address'] = mem.availConst(typee)
		return varTable['constants'][var]


# QUAD GENERATION FUNCTIONS
# ===========================================================================
def gen_goto_main():
	pSaltos.push(Quadruples.cont)
	quad = Quadruple(Quadruples.cont, getOperationCode('Goto'), '', '', '')
	quadruples.addQuad(quad)


def fill_main_quad():
	fill = pSaltos.peek()
	pSaltos.pop()
	quadruples.fillQuad(fill, Quadruples.cont)


def push_false_bottom():
	pilaOptr.push('(')


def pop_false_bottom():
	if pilaOptr.peek() == '(':
		pilaOptr.pop()
	else:
		print "No es un '(' al top de la pilaOptr"
		sys.exit()


def to_pilaOp(var, line, p):
	pilaOp.push(var['address'])
	pTypes.push(var['type'])
	mem.addToMem(var['address'])
	

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
			quad = Quadruple(Quadruples.cont, getOperationCode('='), oper, '', temp)
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
		quad = Quadruple(Quadruples.cont, getOperationCode('read'), '', '', temp)
		quadruples.addQuad(quad)
	else:
		print 'Cant generate read estatement quadruple in line %s' % line


def gen_write_quad(line):
	if pilaOp.size() > 0:
		temp = pilaOp.peek()
		pilaOp.pop()
		pTypes.pop()
		quad = Quadruple(Quadruples.cont, getOperationCode('write'), '', '', temp)
		quadruples.addQuad(quad)
	else:
		print 'Cant generate write estatement quadruple in line %s' % line


def var_assign(p):
	if len(p) > 1:
		line = p.lineno(0)
		var = tryRegisterVar(p[-3])
		to_pilaOp(var, line, p)
		var = tryRegisterVar(p[2])
		to_pilaOp(var, line, p)

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
			quad = Quadruple(Quadruples.cont, getOperationCode('='), oper, '', temp)
			quadruples.addQuad(quad)
		else:
			print "Type mismatch in line %s" % line
			sys.exit()
	else:
		print 'Cant generate assignation estatement quadruple in line %s' % line


def gen_gotof_quad(res):
	quad = Quadruple(Quadruples.cont, getOperationCode('GotoF'), res, '', '')
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
	quad = Quadruple(Quadruples.cont, getOperationCode('Goto'), '', '', ret)
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
			nextTemp = mem.avail(res)
			quad = Quadruple(Quadruples.cont, getOperationCode(oper), lOperand, rOperand, nextTemp)
			quadruples.addQuad(quad)
			pTypes.push(res)
			pilaOp.push(nextTemp)
		else:
			print "Type mismatch in line %s" % line
			sys.exit()


def check_args(p):
	global paramCount
	paramCount += 1
	line = p.lineno(0)
	arg = pilaOp.peek()
	pilaOp.pop()
	argType = pTypes.peek()
	pTypes.pop()
	lastType = dirProcedures[lastFuncCallScope]['args'][paramCount-1]
	if argType != lastType:
		print 'Type mismatch in argument #%s of function %s in line %s, expected %s but recieved %s instead' % (paramCount, lastFuncCallScope, line, lastType, argType)
		sys.exit()
	else:
		quad = Quadruple(Quadruples.cont, getOperationCode('param'), arg, paramCount, '')
		quadruples.addQuad(quad)


def gen_go_sub(p):
	paramsno = dirProcedures[lastFuncCallScope]['params_no']	
	if paramCount != paramsno:
		print 'Function "%s" requires %s parameters' % (lastFuncCallScope, paramsno)
		sys.exit()
	else:
		quad = Quadruple(Quadruples.cont, getOperationCode('gosub'), lastFuncCallScope, "", dirProcedures[lastFuncCallScope]['quad_start'])
		quadruples.addQuad(quad)


def gen_era(p):
	lastscope = p[-3]
	global lastFuncCallScope
	lastFuncCallScope = lastscope
	quad = Quadruple(Quadruples.cont, getOperationCode('era'), '', '', lastscope)
	quadruples.addQuad(quad)


def gen_return_quad(scope, p):
	global returnCount
	line = p.lineno(0)
	ret = pilaOp.peek()
	pilaOp.pop()
	retType = pTypes.peek()
	pTypes.pop()
	if scope == 'main':
		print "Main can't have a return statement"
		sys.exit()
	functype = dirProcedures[scope]['func_type']
	if functype == retType:
		quad = Quadruple(Quadruples.cont, getOperationCode('return'), '', '', ret)
		quadruples.addQuad(quad)
		pReturnSaltos.push(Quadruples.cont)
		quad = Quadruple(Quadruples.cont, getOperationCode('Goto'), '', '', '')
		quadruples.addQuad(quad)
		returnCount += 1
	else:
		print "Type mismatch of return in line %s" % line
		sys.exit()


def gen_endproc_quad(p):
	lastscope = scope[len(scope)-1]
	global returnCount
	while returnCount != 0:
		fill = pReturnSaltos.peek()
		pReturnSaltos.pop()
		quadruples.fillQuad(fill, Quadruples.cont)
		returnCount -= 1
	quad = Quadruple(Quadruples.cont, getOperationCode('Endproc'), '', '','')
	quadruples.addQuad(quad)
	global paramCount
	paramCount = 0


def gen_end_quad():
	quad = Quadruple(Quadruples.cont, getOperationCode('END'), '', '','')
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


# Obtener el codigo de operacion
def getOperationCode(oper):
	return operationCodes[oper]


# Probar que este declarado correctamente el diccionario de operaciones
def printOperationCodes():
	for key in operationCodes:
		print operationCodes[key]


# Desplegar las variables por motivos de debugging
def printAll():
	print "===\t\tVar Table\t\t==="
	pprint.pprint(varTable)
	print "===\t\tDir Proc\t\t==="
	pprint.pprint(dirProcedures)
	#print "===\t\tPila Operadores\t\t==="
	#print 'size', pilaOptr.size()
	#printStack(pilaOptr)
	#print "===\t\tPila Operandos\t\t==="
	#print 'size', pilaOp.size()
	#printStack(pilaOp)
	#print "===\t\tPila Tipos\t\t==="
	#print 'size', pTypes.size()
	#printStack(pTypes)
	#print "===\t\tPila Saltos\t\t==="
	#print 'size', pSaltos.size()
	#printStack(pSaltos)
	#print "===\t\tMemoria\t\t==="
	#mem.printMemory()
	print "===\t\tCuadruplos\t\t==="
	print 'size', quadruples.size()
	quadruples.printQuadruples()
