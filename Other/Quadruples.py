from OperationCodes import *

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

# Clase cuadruplos que 
class Quadruples():
	quadruples = []
	cont = 1

	def addQuad(self, quad):
		self.quadruples.append(quad)
		Quadruples.cont += 1

	def size(self):
		return len(self.quadruples)

	def fillQuad(self, number, info):
		self.quadruples[number-1].result = info

	def printQuadruples(self):
		for quad in self.quadruples:
			quad.printQuadruple()