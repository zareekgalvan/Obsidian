import sys
from Declarations import *

class MemSpace():
	def __init__(self, name, base, longi):
		self.name = name
		self.base = base
		self.long = longi
		self.intsBase = base
		self.intsActual = self.intsBase
		self.doublesBase = base + self.long
		self.doublesActual = self.doublesBase
		self.boolsBase = base + (self.long * 2) 
		self.boolsActual = self.boolsBase
		self.last = self.boolsBase + self.long - 1

	def getNextInt(self):
		if self.intsActual + 1 < self.doublesBase:
			nextInt = self.intsActual
			self.intsActual += 1
			return nextInt
		else:
			print "Memory exceeded"
			sys.exit()

	def getNextDouble(self):
		if self.doublesActual + 1 < self.boolsBase:
			nextDouble = self.doublesActual
			self.doublesActual += 1
			return nextDouble
		else:
			print "Memory exceeded"
			sys.exit()

	def getNextBool(self):
		if self.boolsActual + 1 <= self.last:
			nextBool = self.boolsActual
			self.boolsActual += 1
			return nextBool
		else:
			print "Memory exceeded"
			sys.exit()

	def deleteMemSpace(self):
		self.intsActual = self.intsBase
		self.doublesActual = self.doublesBase
		self.boolsActual = self.boolsBase

	def getSpaceMemType(self, address):
		if address >= self.base and address < self.doublesBase:
			return 'int'
		elif address >= self.doublesBase and address < self.boolsBase:
			return 'double'
		elif address >= self.boolsBase and address <= self.last:
			return 'bool'

	def printMemSpace(self):
		print "Name:", self.name
		print "Longitude:", self.long
		print "Base ints:", self.intsBase
		print "Act ints:", self.intsActual
		print "Base doubles:", self.doublesBase
		print "Act doubles:", self.doublesActual
		print "Base bools:", self.boolsBase
		print "Act bools:", self.boolsActual
		print "Last direction:", self.last, "\n"


class Memory():

	def __init__(self):
		self.memory = {}
		self.globalMem = MemSpace('global', 0, 500)
		self.variableMem = MemSpace('variables', self.globalMem.long + self.globalMem.boolsBase, 1000)
		self.temporalMem = MemSpace('temporals', self.variableMem.long + self.variableMem.boolsBase, 1500)
		self.constantMem = MemSpace('constants', self.temporalMem.long + self.temporalMem.boolsBase, 1000)
		self.memory['global'] = {}
		self.memory['variable'] = Stack()
		self.memory['variable'].push({})
		self.memory['temporal'] = Stack()
		self.memory['temporal'].push({})
		self.memory['constant'] = {}

	def avail(self, typee):
		nextTemp = None
		global scope
		if scope[len(scope)-1] == 'global':
			if typee == 'bool':
				nextTemp = self.globalMem.getNextBool()
			elif typee == 'double':
				nextTemp = self.globalMem.getNextDouble()
			elif typee == 'int':
				nextTemp = self.globalMem.getNextInt()
		else:
			if typee == 'bool':
				nextTemp = self.temporalMem.getNextBool()
			elif typee == 'double':
				nextTemp = self.temporalMem.getNextDouble()
			elif typee == 'int':
				nextTemp = self.temporalMem.getNextInt()
		return nextTemp

	def availVar(self, typee):
		nextTemp = None
		if typee == 'bool':
			nextTemp = self.variableMem.getNextBool()
		elif typee == 'double':
			nextTemp = self.variableMem.getNextDouble()
		elif typee == 'int':
			nextTemp = self.variableMem.getNextInt()
		return nextTemp

	def availConst(self, typee):
		nextTemp = None
		if typee == 'bool':
			nextTemp = self.constantMem.getNextBool()
		elif typee == 'double':
			nextTemp = self.constantMem.getNextDouble()
		elif typee == 'int':
			nextTemp = self.constantMem.getNextInt()
		return nextTemp

	def deleteMems(self):
		self.variableMem.deleteMemSpace()
		self.temporalMem.deleteMemSpace()

	def addToMem(self, dir, val = None):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			self.memory['global'][dir] = val
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			self.memory['variable'].pushToDict(dir, val)
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			self.memory['temporal'].pushToDict(dir, val)
		elif dir >= self.constantMem.base and dir <= self.constantMem.last:
			self.memory['constant'][dir] = val

	def getValFromMem(self, dir):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			return self.memory['global'][dir]
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			return self.memory['variable'].peekFromDict(dir)
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			return self.memory['temporal'].peekFromDict(dir)
		elif dir >= self.constantMem.base and dir <= self.constantMem.last:
			return self.memory['constant'][dir]

	def putValInMem(self, dir, val):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			self.memory['global'][dir] = val
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			self.memory['variable'].pushToDict(dir, val)
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			self.memory['temporal'].pushToDict(dir, val)
		elif dir >= self.constantMem.base and dir <= self.constantMem.last:
			self.memory['constant'][dir] = val

	def getTypeFromMem(self, dir):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			return self.globalMem.getSpaceMemType(dir)
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			return self.variableMem.getSpaceMemType(dir)
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			return self.temporalMem.getSpaceMemType(dir)
		elif dir >= self.constantMem.base and dir <= self.constantMem.last:
			return self.constantMem.getSpaceMemType(dir)

	def printMemory(self):
		self.globalMem.printMemSpace()
		self.variableMem.printMemSpace()
		self.temporalMem.printMemSpace()
		self.constantMem.printMemSpace()
		for key in self.memory:
			if type(self.memory[key]) is dict:
				print self.memory[key]
			else:
				printStack(self.memory[key])
			
