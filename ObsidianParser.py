import ply.yacc as yacc

# Importar tokens del lexer
from ObsidianLex import tokens
# Importar la clase cuadruplos y sus operaciones
from Other.Functions import *
from Other.VirtualMachine import *

# Definicion de las reglas
def p_program(p):
	'''program : gen_goto_main more_vars more_func main'''
	p[0] = "PROGRAM COMPILED"

def p_gen_goto_main(p):
	'''gen_goto_main :'''
	varTable['constants'] = {}
	gen_goto_main()

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
	'''vars_aux : ID to_var_table arr var_assign more_vars_aux'''
	p[0] = p[-1]

def p_to_var_table(p):
	'''to_var_table :'''
	to_var_table(p) 

def p_var_assign(p):
	'''var_assign : EQUALS var_cte
			|'''
	var_assign(p)

def p_more_vars_aux(p):
	'''more_vars_aux : COMMA vars_aux
			|'''

def p_arr(p):
	'''arr : LSQRTBRACKET const register_space RSQRTBRACKET
			|'''

	check_arr_param(p)

def p_register_space(p):
	'''register_space :'''
	register_space(p)

def p_var_cte(p):
	'''var_cte : const to_pilaOp
			| ID to_pilaOp arr_par
			| func_call to_pilaOp'''
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
	to_proc_dir(p) 

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
	varid = p[-1]
	vartype = p[-2]
	line = p.lineno(0)
	to_args(varid, vartype, line, p)

def p_func_block(p):
	'''func_block : LBRACKET more_vars actual_quad_no more_statement gen_endproc_quad RBRACKET'''

def p_actual_quad_no(p):
	'''actual_quad_no :'''
	lastscope = scope[len(scope)-1]
	actual_quad_no(lastscope)

def p_gen_endproc_quad(p):
	'''gen_endproc_quad :'''
	gen_endproc_quad(p)
	mem.deleteMems()

def p_more_statement(p):
	'''more_statement : statement more_statement
			|'''

def p_statement(p):
	'''statement : read
		| write
		| return_stmt
		| cycle
		| condition
		| assignation
		| func_call SEMICOLON'''

def p_read(p):
	'''read : READ LPAR ID to_pilaOp arr_par RPAR gen_read_quad SEMICOLON'''

def p_gen_read_quad(p):
	'''gen_read_quad :'''
	line = p.lineno(0)
	gen_est_quad(line, 'read')

def p_write(p):
	'''write : WRITE LPAR exp RPAR gen_write_quad SEMICOLON'''

def p_gen_write_quad(p):
	'''gen_write_quad :'''
	line = p.lineno(0)
	gen_est_quad(line, 'write')

def p_return_stmt(p):
	'''return_stmt : RETURN exp gen_return_quad SEMICOLON'''

def p_gen_return_quad(p):
	'''gen_return_quad :'''
	lastscope = scope[len(scope)-1]
	gen_return_quad(lastscope, p)


def p_cycle(p):
	'''cycle : WHILE cycle_start LPAR expression RPAR check_type block cycle_end'''

def p_cycle_start(p):
	'''cycle_start :'''
	cycle_start()

def p_cycle_end(p):
	'''cycle_end :'''
	cycle_end()

def p_condition(p):
	'''condition : IF LPAR expression RPAR check_type block else_posible fill_end_condition'''

def p_else_posible(p):
	'''else_posible : ELSE gen_goto block
			|'''

def p_gen_goto(p):
	'''gen_goto :'''
	gen_goto()

def p_fill_end_condition(p):
	'''fill_end_condition :'''
	fill_end_condition()

def p_check_type(p):
	'''check_type :'''
	check_type(p)

def p_assignation(p):
	'''assignation : ID to_pilaOp arr_par EQUALS expression gen_assignation_quad SEMICOLON'''

def p_gen_assignation_quad(p):
	'''gen_assignation_quad :'''
	line = p.lineno(0)
	gen_est_quad(line, 'assignation')

def p_func_call(p):
	'''func_call : ID is_valid_func LPAR gen_era push_false_bottom params pop_false_bottom RPAR gen_go_sub'''
	p[0] = p[1]

def p_params(p):
	'''params : exp check_args more_params
			|'''

def p_more_params(p):
	'''more_params : COMMA exp check_args more_params
			|'''

def p_check_args(p):
	'''check_args :'''
	check_args(p)

def p_is_valid_func(p):
	'''is_valid_func :'''
	is_valid_func(p)

def p_gen_era(p):
	'''gen_era :'''
	gen_era(p)

def p_gen_go_sub(p):
	'''gen_go_sub :'''
	gen_go_sub(p)

def p_block(p):
	'''block : LBRACKET more_statement RBRACKET'''

def p_arr_par(p):
	'''arr_par : LSQRTBRACKET exp RSQRTBRACKET 
			|'''
	if len(p) > 1:
		gen_ver_quad(p)

def p_expression(p):
	'''expression : conc gen_conc_quad expression_aux'''
	p[0] = p[1]

def p_expression_aux(p):
	'''expression_aux : ao add_to_pilaOptr conc gen_conc_quad expression_aux
			|'''
def p_gen_conc_quad(p):
	'''gen_conc_quad :'''
	line = p.lineno(0)
	gen_exp_quad(line, 'conc')

def p_conc(p):
	'''conc : exp gen_comp_quad conc_aux'''
	p[0] = p[1]

def p_conc_aux(p):
	'''conc_aux : comp add_to_pilaOptr exp gen_comp_quad
				|'''

def p_gen_comp_quad(p):
	'''gen_comp_quad :'''
	line = p.lineno(0)
	gen_exp_quad(line, 'comp')

def p_exp(p):
	'''exp : term gen_term_quad exp_aux'''
	p[0] = p[1]

def p_exp_aux(p):
	'''exp_aux : pl add_to_pilaOptr term gen_term_quad exp_aux
			|'''

def p_gen_term_quad(p):
	'''gen_term_quad :'''
	line = p.lineno(0)
	gen_exp_quad(line, 'term')

def p_term(p):
	'''term : factor gen_factor_quad term_aux'''
	p[0] = p[1]

def p_term_aux(p):
	'''term_aux : dm add_to_pilaOptr factor gen_factor_quad term_aux
			|'''

def p_gen_factor_quad(p):
	'''gen_factor_quad :'''
	line = p.lineno(0)
	gen_exp_quad(line, 'factor')

def p_factor(p):
	'''factor : LPAR add_to_pilaOptr expression RPAR pop_false_bottom
			| var_cte'''
	if p[1] != '(':
		p[0] = p[1]
	else:
		p[0] = p[3]

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
	if var == None:
		var = p[-2]
	var = tryRegisterVar(var)
	val = None
	if type(p[-1]) == int or type(p[-1]) == float or p[-1] == 'true' or p[-1] == 'false':
		val = p[-1]
	to_pilaOp(var, val, line, p)

def p_add_to_pilaOptr(p):
	'''add_to_pilaOptr :'''
	pilaOptr.push(p[-1])

def p_push_false_bottom(p):
	'''push_false_bottom :'''
	push_false_bottom()

def p_pop_false_bottom(p):
	'''pop_false_bottom :'''
	pop_false_bottom()
	global paramCount
	paramCount = 0

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
	fill_main_quad()

def p_main_block(p):
	'''main_block : LBRACKET more_vars more_statement RBRACKET gen_end_quad'''
def p_gen_end_quad(p):
	'''gen_end_quad :'''
	gen_end_quad()

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
				if debug == 'on':
					printAll()

				#print "Valid syntax"
				virtualMachine = VirtualMachine()
				virtualMachine.execute(quadruples.quadruples)
				mem.printMemory()
				#mem.memory['variable'].printStack()
				#pprint.pprint(varTable)
				#print mem.memory['']
				#print pDim.peek()
				print mem.getValFromMem(101500)

		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')