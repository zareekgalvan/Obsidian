import ply.lex as lex

# Lista de palabras reservadas

reserved = {
	'int' : 'INT',
	'double' : 'DOUBLE',
	'bool' : 'BOOL',
	'func' : 'FUNC',
	'void' : 'VOID',
	'if' : 'IF',
	'main' : 'MAIN',
	'while' : 'WHILE',
	'read' : 'READ',
	'write' : 'WRITE',
	'true' : 'TRUE',
	'false' : 'FALSE',
	'return' : 'RETURN'
}

# Lista de tokens

tokens = ['PLUS', 'MINUS', 'MULTIPLICATION', 'DIVISION', 'MOD', 'EQUALS', 
			'EQUALEQUALS', 'DIFFERENT', 'GREATER', 'LESS', 
			'GREATEROREQUAL', 'LESSOREQUAL', 'AND', 'OR', 'LPAR', 'RPAR', 
			'LBRACKET', 'RBRACKET','LSQRTBRACKET', 'RSQRTBRACKET', 'COMMA', 'SEMICOLON', 'CTEINT', 
			'CTEDOUBLE', 'CTEBOOL', 'ID'] + list(reserved.values())

# Expresiones regulares

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'
t_MOD = r'%'
t_EQUALS = r'='
t_EQUALEQUALS = r'=='
t_DIFFERENT = r'<>'
t_GREATER = r'>'
t_LESS = r'<'
t_GREATEROREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_LSQRTBRACKET = r'\['
t_RSQRTBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_CTEINT = r'-?[0-9]+'
t_CTEDOUBLE = r'-?[0-9]+\.[0-9]+'
t_CTEBOOL = r'true|false'

# Expresion regular para los IDs

def t_ID(t):
	r'[a-z][a-zA-Z0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

# Identificar saltos de linea y llevar conteo de la linea actual

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Manejo de errores de lexico

def t_error(t):
	print("Error de lexico %s" % t.value[0])
	exit(-1)
	t.lexer.skip(1)

# Comentarios estilo C++

def t_comment(t):
    r'//.*\n'
    t.lexer.lineno += 1
    return t


# Crear el analizador de lexico

lexer = lex.lex()