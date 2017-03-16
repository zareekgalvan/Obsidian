from Structs import *
import pprint

# Tabla de Variables
scope = ['global']
lastType = []
varTable = {}
varTable[scope[len(scope)-1]] = {}

# Directorio de procedimientos
dirProcedures = {}

# Pilas
pilaOp = Stack()
pilaOptr = Stack()
pSaltos = Stack()
pTypes = Stack()

def printAll():
	#print "===Var Table==="
	#pprint.pprint(varTable)
	#print "===Dir Proc==="
	#pprint.pprint(dirProcedures)
	print("===Pila Operadores===")
	print(pilaOptr.size())
	printStack(pilaOptr)
	print("===Pila Operandos===")
	print(pilaOp.size())
	printStack(pilaOp)
	print("===Pila tipos===")
	print(pTypes.size())
	printStack(pTypes)