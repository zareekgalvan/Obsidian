import ply.yacc as yacc
import sys

# Importar tokens del lexer
from ObsidianLex import tokens

# Tabla de Variables
scope = ['global']
lastType = []
varTable = {}
varTable[scope[len(scope)-1]] = {}
# Directorio de procedimientos
dirProcedures = {}


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
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  lastType[len(lastType)-1]
	else:
		print('Variable "%s" already registered' % (varid))
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
	'''var_cte : CTEINT
			| CTEDOUBLE
			| CTEBOOL
			| ID arr
			| func_call'''

def p_const(p):
	'''const : CTEINT
			| CTEDOUBLE
			| CTEBOOL'''

def p_more_func(p):
	'''more_func : func
			|'''

def p_func(p):
	'''func : FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_func'''

def p_to_proc_dir(p):
	'''to_proc_dir :'''
	procname = p[-1]
	if procname not in scope:
		scope.append(procname)
		varTable[procname] = {}
		dirProcedures[procname] = {}
		dirProcedures[procname]['func_type'] = p[-2]
		dirProcedures[procname]['args'] = []
	else:
		print('Function "%s" already registered' % (procname))
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
	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
		varTable[scope[len(scope)-1]][varid] =  vartype
	else:
		print('Variable "%s" already registered' % (varid))
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
	'''assignation : ID arr_par EQUALS assign SEMICOLON'''

def p_assign(p):
	'''assign : expression
			| func_call'''

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
	'''expression_aux : ao conc expression_aux
			|'''

def p_conc(p):
	'''conc : exp conc_aux'''

def p_conc_aux(p):
	'''conc_aux : comp exp
				|'''

def p_exp(p):
	'''exp : term exp_aux'''

def p_exp_aux(p):
	'''exp_aux : pl term exp_aux
			|'''

def p_term(p):
	'''term : factor term_aux'''

def p_term_aux(p):
	'''term_aux : dm factor term_aux
			|'''

def p_factor(p):
	'''factor : LPAR expression RPAR
			| var_cte'''

def p_ao(p):
	'''ao : AND
			| OR'''

def p_comp(p):
	'''comp : GREATER
			| LESS
			| GREATEROREQUAL
			| LESSOREQUAL
			| EQUALEQUALS
			| DIFFERENT'''

def p_pl(p):
	'''pl : PLUS
			| MINUS'''

def p_dm(p):
	'''dm : MULTIPLICATION
			| DIVISION
			| MOD'''



def p_main(p):
	'''main : MAIN main_block'''

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
				#print varTable
				#print dirProcedures
				print "Valid syntax"

		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')