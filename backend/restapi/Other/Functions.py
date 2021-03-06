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
	varid = p[-1]
	line = p.lineno(0)
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] = {}
		varTable[scope[len(scope)-1]][varid]['type'] =  lastType[len(lastType)-1]
		if scope[len(scope)-1] != 'global':
			address = mem.availVar(varTable[scope[len(scope)-1]][varid]['type'])
		else:
			address = mem.availGlobal(varTable[scope[len(scope)-1]][varid]['type'])
		varTable[scope[len(scope)-1]][varid]['address'] = address
		varTable[scope[len(scope)-1]][varid]['dim'] = 0
		mem.addToMem(address)
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
		varTable['global'][procname]['address'] = mem.availGlobal(functype)
		varTable['global'][procname]['dim'] = 0
		varTable[procname] = {}
		dirProcedures[procname] = {}
		dirProcedures[procname]['func_type'] = functype
		dirProcedures[procname]['args'] = []
		dirProcedures[procname]['quad_start'] = Quadruples.cont
		#print procname, varTable['global'][procname]['address']
		mem.addToMem(varTable['global'][procname]['address'])
	else:
		print 'Function "%s" already registered in line %s' % (procname, line)
		sys.exit()


def to_args(varid, vartype, line, p):
	dirProcedures[scope[len(scope)-1]]['args'].append(vartype)
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  {}
		varTable[scope[len(scope)-1]][varid]['type'] = vartype
		varTable[scope[len(scope)-1]][varid]['address'] = mem.availVar(vartype)
		varTable[scope[len(scope)-1]][varid]['param_no'] = len(dirProcedures[scope[len(scope)-1]]['args'])
		varTable[scope[len(scope)-1]][varid]['dim'] = 0
	else:
		print 'Variable "%s" in line %s already registered' % (varid, line)
		sys.exit() 


def actual_quad_no(scope):
	dirProcedures[scope]['params_no'] = len(dirProcedures[scope]['args'])
	dirProcedures[scope]['vars_no'] = len(varTable[scope]) - dirProcedures[scope]['params_no']


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


def register_space(p):
	varid = p[-4]
	varTable[scope[len(scope)-1]][varid]['dim'] = {}
	varTable[scope[len(scope)-1]][varid]['dim']['liminf'] = 0
	varTable[scope[len(scope)-1]][varid]['dim']['limsup'] = p[-1] - 1
	i = 0
	add = tryRegisterVar(p[-1])
	mem.addToMem(add['address'], p[-1])
	while i < varTable[scope[len(scope)-1]][varid]['dim']['limsup']:
		if scope[len(scope)-1] != 'global':
			address = mem.availVar(varTable[scope[len(scope)-1]][varid]['type'])
		else:
			address = mem.availGlobal(varTable[scope[len(scope)-1]][varid]['type'])
		varTable[scope[len(scope)-1]][address] = {}
		varTable[scope[len(scope)-1]][address]['type'] = varTable[scope[len(scope)-1]][varid]['type']
		varTable[scope[len(scope)-1]][address]['address'] = address
		mem.addToMem(address)
		mem.putValInMem(address, 0)
		mem.putValInMem(address -1, 0)
		i += 1

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


def to_pilaOp(var, val, line, p):
	pilaOp.push(var['address'])
	pTypes.push(var['type'])
	mem.addToMem(var['address'], val)
	

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
		val = None
		if type(p[-3]) == int or type(p[-3]) == float or p[-3] == 'true' or p[-3] == 'false':
			val = p[-3]
		to_pilaOp(var, val, line, p)
		var = tryRegisterVar(p[2])
		val = None
		if type(p[2]) == int or type(p[2]) == float or p[2] == 'true' or p[2] == 'false':
			val = p[2]
		to_pilaOp(var, val, line, p)

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
			nextTemp = mem.availTemp(res)
			varTable[scope[len(scope)-1]][nextTemp] = {}
			varTable[scope[len(scope)-1]][nextTemp]['address'] = nextTemp
			varTable[scope[len(scope)-1]][nextTemp]['type'] = res
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
	global paramCount
	paramsno = dirProcedures[lastFuncCallScope]['params_no']
	if paramCount != paramsno:
		print 'Function "%s" requires %s parameters' % (lastFuncCallScope, paramsno)
		sys.exit()
	else:
		quad = Quadruple(Quadruples.cont, getOperationCode('gosub'), lastFuncCallScope, "", dirProcedures[lastFuncCallScope]['quad_start'])
		quadruples.addQuad(quad)
	paramCount = 0


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
		print "Type mismatch of return in line %s: %s" % (line, retType)
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


def gen_ver_quad(p):
	info = tryRegisterVar(p[2])
	dim = None
	if isArray(p[-2]):
		dim = 1
		pDim.push({p[-2] : dim})
		dim = getDim(getScopeFromID(p[-2]), p[-2])
		push_false_bottom()
	else:
		print "%s is not an array" % p[-2]
		sys.exit()
	pilaOp.pop()
	#print info['address'], 'es la const'
	quad = Quadruple(Quadruples.cont, getOperationCode('ver'), info['address'], dim['liminf'], dim['limsup'])
	quadruples.addQuad(quad)

	#print 11, pilaOp.peek(), getID(pilaOp.peek())
	var = pilaOp.peek()
	pilaOp.pop()
	var2 = tryRegisterVar(var)
	mem.addToMem(var2['address'], var)
	typee = pTypes.peek()
	pTypes.pop()
	res = getType(typee, info['type'], '+')
	if res != 'ERROR':
		nextTemp = mem.availTemp(res)
		#print nextTemp, "im avail in line %s" % p.lineno(0)
		varTable[scope[len(scope)-1]][nextTemp] = {}
		varTable[scope[len(scope)-1]][nextTemp]['address'] = nextTemp
		varTable[scope[len(scope)-1]][nextTemp]['type'] = res
		mem.addToMem(nextTemp)
		nextTemp = '(' + str(nextTemp) + ')'
		quad = Quadruple(Quadruples.cont, getOperationCode('+'), var2['address'], info['address'], nextTemp)
		quadruples.addQuad(quad)
		pTypes.push(res)
		pilaOp.push(nextTemp)
		pilaOptr.pop()
		pDim.pop()
	else:
		print "Type mismatch in line %s" % p.lineno(0)
		sys.exit()



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


def isInt(number):
	try:
		return type(int(number)) is int
	except ValueError:
		return False


def isDouble(number):
	try:
		return type(float(number)) is float
	except ValueError:
		return False


def getVirtualVariblesFromVarTable(scope):
	dirr = {}
	for key in varTable:
		if key == scope:
			for val in varTable[key]:
				if not isInt(val):
					dirr[varTable[key][val]['address']] = None
	return dirr


def getVirtualTemporalsFromVarTable(scope):
	dirr = {}
	for key in varTable:
		if key == scope:
			for val in varTable[key]:
				if isInt(val):
					dirr[varTable[key][val]['address']] = None
	return dirr


def tryGetAddressFromParamNo(scope, paramNo):
	for key in varTable:
		if key == scope:
			for val in varTable[key]:
				if not isInt(val) and isParam(scope, val):
					if varTable[key][val]['param_no'] == paramNo:
						return varTable[key][val]['address']


def isParam(scope, val):
	try:
		address = varTable[scope][val]['param_no']
		return True
	except KeyError:
		return False


def getID(address):
	for key in varTable['global']:
		if varTable['global'][key]['address'] == address:
			return key
	for key in varTable[scope[len(scope)-1]]:
		if varTable[scope[len(scope)-1]][key]['address'] == address:
			return key
	for key in varTable['constants']:
		if varTable['constants'][key]['address'] == address:
			return key
	return None


def getScopeFromID(varid):
	if varid in varTable['global']:
		return 'global'
	elif varid in varTable[scope[len(scope)-1]]:
		return scope[len(scope)-1]
	elif varid in varTable['constants']:
		return 'constants'


def getDim(scope, varid):
	return varTable[scope][varid]['dim']


def isArray(varid):
	if varid in varTable['global']:
		return verIfArray('global', varid)
	elif varid in varTable[scope[len(scope)-1]]:
		return verIfArray(scope[len(scope)-1], varid)
	elif varid in varTable['constants']:
		return verIfArray('constants', varid)


def verIfArray(scope, varid):
	try:
		dim = varTable[scope][varid]['dim'] != 0
		return dim
	except KeyError:
		return False


# Desplegar las variables por motivos de debugging
def printAll():
	print "===\t\tVar Table\t\t==="
	pprint.pprint(varTable)
	print "===\t\tDir Proc\t\t==="
	pprint.pprint(dirProcedures)
	'''print "===\t\tPila Operadores\t\t==="
	print 'size', pilaOptr.size()
	pilaOptr.printStack()
	print "===\t\tPila Operandos\t\t==="
	print 'size', pilaOp.size()
	pilaOp.printStack()
	print "===\t\tPila Tipos\t\t==="
	print 'size', pTypes.size()
	pTypes.printStack()
	print "===\t\tPila Saltos\t\t==="
	print 'size', pSaltos.size()
	pSaltos.printStack()
	print "===\t\tMemoria\t\t==="
	mem.printMemory()'''
	print "===\t\tCuadruplos\t\t==="
	print 'size', quadruples.size()
	quadruples.printQuadruples()
