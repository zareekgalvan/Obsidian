from OperationCodes import *

# Clase cuadruplo para la generacion de codigo intermedio
class Quadruple:
	def __init__(self, operator, left, right, temp):
		self.optr = operator
		self.opLeft = left
		self.opRight = right
		self.result = temp

	def printQuadruple(self):
		print "[\t", self.optr, '\t', self.opLeft, '\t', self.opRight, '\t', self.result, '\t', "]"

# Clase cuadruplos que 
class Quadruples():
	quadruples = []
	cont = 0

	def addQuad(self, quad):
		self.quadruples.append(quad)

	def size(self):
		return len(self.quadruples)

	def printQuadruples(self):
		for quad in self.quadruples:
			quad.printQuadruple()