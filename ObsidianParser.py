import ply.yacc as yacc
import sys

# Importar tokens del lexer
from ObsidianLex import tokens
# Importar la clase cuadruplos y sus operaciones
from Other.Quadruples import *

# Definicion de las reglas
def p_program(p):
	'''program : more_vars more_func main'''
	p[0] = "PROGRAM COMPILED"

def p_more_vars(p):
	'''more_vars : vars
			|'''

def p_vars(p):
	'''vars : var_type vars_aux SEMICOLON more_vars'''

def p_var_type(p):
	'''var_type : BOOL
			| INT
			| DOUBLE'''
	p[0] = p[1]
	lastType.append(p[1])

def p_vars_aux(p):
	'''vars_aux : ID arr to_var_table var_assign more_vars_aux'''
	p[0] = p[-1]

def p_to_var_table(p):
	'''to_var_table :'''
	varid = p[-2]
	line = p.lineno(0)
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  lastType[len(lastType)-1]
	else:
		print('Variable "%s" in line %s already registered' % (varid, line))
		sys.exit() 

def p_var_assign(p):
	'''var_assign : EQUALS var_cte
			|'''

def p_more_vars_aux(p):
	'''more_vars_aux : COMMA vars_aux
			|'''

def p_arr(p):
	'''arr : LSQRTBRACKET const RSQRTBRACKET arr
			|'''

def p_var_cte(p):
	'''var_cte : const
			| ID arr
			| func_call'''
	p[0] = p[1]

def p_const(p):
	'''const : CTEINT
			| CTEDOUBLE
			| CTEBOOL'''
	p[0] = p[1]

def p_more_func(p):
	'''more_func : func
			|'''

def p_func(p):
	'''func : FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_func'''

def p_to_proc_dir(p):
	'''to_proc_dir :'''
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

def p_func_type(p):
	'''func_type : VOID 
			| BOOL
			| INT
			| DOUBLE'''
	p[0] = p[1]

def p_arguments(p):
	'''arguments : var_type ID to_args more_args
			|'''
	

def p_more_args(p):
	'''more_args : COMMA var_type ID to_args more_args
			|'''

def p_to_args(p):
	'''to_args :'''
	dirProcedures[scope[len(scope)-1]]['args'].append(p[-2])
	varid = p[-1]
	vartype = p[-2]
	line = p.lineno(0)
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  vartype
	else:
		print('Variable "%s" in line %s already registered' % (varid, line))
		sys.exit() 

def p_func_block(p):
	'''func_block : LBRACKET more_vars more_statement optional_return RBRACKET'''

def p_optional_return(p):
	'''optional_return : RETURN exp SEMICOLON
			|'''

def p_more_statement(p):
	'''more_statement : statement more_statement
			|'''

def p_statement(p):
	'''statement : read
		| write
		| cicle
		| condition
		| assignation
		| func_call SEMICOLON'''

def p_read(p):
	'''read : READ LPAR ID arr_par RPAR SEMICOLON'''

def p_write(p):
	'''write : WRITE LPAR exp RPAR SEMICOLON'''

def p_cicle(p):
	'''cicle : WHILE LPAR expression RPAR block'''

def p_condition(p):
	'''condition : IF LPAR expression RPAR block else_posible'''

def p_else_posible(p):
	'''else_posible : ELSE block
			|'''

def p_assignation(p):
	'''assignation : ID arr_par EQUALS expression SEMICOLON'''

def p_func_call(p):
	'''func_call : ID LPAR params RPAR'''

def p_params(p):
	'''params : exp more_params
			|'''

def p_more_params(p):
	'''more_params : COMMA exp more_params
			|'''

def p_block(p):
	'''block : LBRACKET more_statement RBRACKET'''

def p_arr_par(p):
	'''arr_par : LSQRTBRACKET exp RSQRTBRACKET arr_par
			|'''

def p_expression(p):
	'''expression : conc expression_aux'''

def p_expression_aux(p):
	'''expression_aux : ao add_to_pilaOptr conc expression_aux
			|'''

def p_conc(p):
	'''conc : exp conc_aux'''

def p_conc_aux(p):
	'''conc_aux : comp add_to_pilaOptr exp
				|'''

def p_exp(p):
	'''exp : term exp_aux'''

def p_exp_aux(p):
	'''exp_aux : pl add_to_pilaOptr term exp_aux
			|'''

def p_term(p):
	'''term : factor term_aux'''

def p_term_aux(p):
	'''term_aux : dm add_to_pilaOptr factor term_aux
			|'''

def p_factor(p):
	'''factor : LPAR add_to_pilaOptr expression RPAR pop_false_bottom
			| var_cte to_pilaOp'''

def p_ao(p):
	'''ao : AND
			| OR'''
	p[0] = p[1]

def p_comp(p):
	'''comp : GREATER
			| LESS
			| GREATEROREQUAL
			| LESSOREQUAL
			| EQUALEQUALS
			| DIFFERENT'''
	p[0] = p[1]

def p_pl(p):
	'''pl : PLUS
			| MINUS'''
	p[0] = p[1]

def p_to_pilaOp(p):
	'''to_pilaOp :'''
	#hacer validaciones de tipo
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

def p_add_to_pilaOptr(p):
	'''add_to_pilaOptr :'''
	pilaOptr.push(p[-1])

def p_pop_false_bottom(p):
	'''pop_false_bottom :'''
	if pilaOptr.peek() == '(':
		pilaOptr.pop()
	'''else:
		print "No es un '(' al top del pilaOptr"
		sys.exit()'''

def p_dm(p):
	'''dm : MULTIPLICATION
			| DIVISION
			| MOD'''
	p[0] = p[1]

def p_main(p):
	'''main : MAIN main_to_proc_dir main_block'''

def p_main_to_proc_dir(p):
	'''main_to_proc_dir :'''
	procname = p[-1]
	scope.append(procname)
	varTable[procname] = {}

def p_main_block(p):
	'''main_block : LBRACKET more_vars more_statement RBRACKET'''

def p_error(p):
    print('Syntax error in token %s with value \"%s\" in line %s' % (p.type, p.value, p.lineno))
    sys.exit()


# Construir el parser
drawyparser = yacc.yacc()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		file = sys.argv[1]
		# Abre el archivo, almacena su informacion y lo cierra
		try:
			f = open(file,'r')
			data = f.read()
			f.close()
			
			# Parsear el contenido
			
			if (drawyparser.parse(data, tracking=True) == 'PROGRAM COMPILED'):
				#printAll()
				print "Valid syntax"

		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')