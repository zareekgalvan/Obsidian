import ply.yacc as yacc

# Importar tokens del lexer
from ObsidianLex import tokens
# Importar la clase cuadruplos y sus operaciones
from Other.Functions import *

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
	to_var_table(p) 

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
	to_args(p)

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

def p_cicle(p):
	'''cicle : WHILE LPAR expression RPAR block'''

def p_gen_cicle_quad(p):
	'''gen_cicle_quad :'''
	line = p.lineno(0)
	gen_est_quad(line, 'cicle')

def p_condition(p):
	'''condition : IF LPAR expression RPAR block else_posible'''

def p_else_posible(p):
	'''else_posible : ELSE block
			|'''

def p_assignation(p):
	'''assignation : ID arr_par EQUALS expression gen_assignation_quad SEMICOLON'''

def p_gen_assignation_quad(p):
	'''gen_assignation_quad :'''
	line = p.lineno(0)
	gen_est_quad(line, 'assignation')

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
			| var_cte to_pilaOp'''
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
	to_pilaOp(var, line, p)

def p_add_to_pilaOptr(p):
	'''add_to_pilaOptr :'''
	pilaOptr.push(p[-1])

def p_pop_false_bottom(p):
	'''pop_false_bottom :'''
	pop_false_bottom()

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
				if debug == 'on':
					printAll()

				print "Valid syntax"

		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')