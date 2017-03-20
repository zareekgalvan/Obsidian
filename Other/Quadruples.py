from OperationCodes import *
from SemanticCube import *
from Declarations import *

# Clase cuadruplo para la generacion de codigo intermedio
class Quadruple:
	def __init__(self, operator, left, right, temp):
		self.optr = operator
		self.opLeft = left
		self.opRight = right
		self.result = temp

	def printQuad(self):
		print "[", self.optr, self.opLeft, self.opRight, self.result, "]"

quadruples = []

def printCuadruples():
	for quad in quadruples:
		quad.printQuad()
def printAll():
	print "===Var Table==="
	pprint.pprint(varTable)
	print "===Dir Proc==="
	pprint.pprint(dirProcedures)
	print("===Pila Operadores===")
	#print(pilaOptr.size())
	printStack(pilaOptr)
	print("===Pila Operandos===")
	#print(pilaOp.size())
	printStack(pilaOp)
	print("===Pila tipos===")
	#print(pTypes.size())
	printStack(pTypes)
	print("===Cuadruplos===")
	printCuadruples()