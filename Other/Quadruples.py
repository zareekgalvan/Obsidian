from OperationCodes import *
from SemanticCube import *
from Structs import *

pilaOp = Stack()
pilaOptr = Stack()
pSaltos = Stack()
pTypes = Stack()

# Clase cuadruplo para la generacion de codigo intermedio
class Quadruple:
	def __init__(self, operator, left, right, temp):
		self.optr = operator
		self.opLeft = left
		self.opRight = right
		self.result = temp

quadruples = []

