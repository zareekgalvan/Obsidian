from OperationCodes import *
import sys
# Clase cuadruplo para la generacion de codigo intermedio
class Quadruple:

	def __init__(self, number, operator, left, right, temp):
		self.optr = operator
		self.opLeft = left
		self.opRight = right
		self.result = temp
		self.number = number

	def printQuadruple(self):
		print self.number, "\t[\t", self.optr, '\t', self.opLeft, '\t', self.opRight, '\t', self.result, '\t', "]"

# Clase cuadruplos que agrupa la clase cuadruplo
class Quadruples():
	quadruples = []
	cont = 1

	def addQuad(self, quad):
		if isinstance(quad, Quadruple):
			Quadruples.quadruples.append(quad)
			Quadruples.cont += 1
		else:
			print "'%s'is not cuadruple" % quad
			sys.exit()

	def size(self):
		return len(self.quadruples)

	def fillQuad(self, number, info):
		Quadruples.quadruples[number-1].result = info

	def printQuadruples(self):
		for quad in self.quadruples:
			quad.printQuadruple()