import ply.yacc as yacc
import sys

# Importar tokens del lexer
from ObsidianLex import tokens

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

def p_vars_aux(p):
	'''vars_aux : ID arr var_assign more_vars_aux'''

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
	'''func : '''

def p_func_call(p):
	'''func_call : '''

def p_main(p):
	'''main : '''



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
			# print data
			f.close()
			# Parsear el contenido
			
			if (drawyparser.parse(data, tracking=True) == 'PROGRAM COMPILED'):
				print "Valid syntax"

		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')