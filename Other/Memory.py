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
		self.pointerBase = base + (self.long * 3)
		self.pointerActual = self.pointerBase
		self.last = self.pointerBase + self.long - 1

	def getNextInt(self):
		if self.intsActual + 1 < self.doublesBase:
			nextInt = self.intsActual
			self.intsActual += 1
			return nextInt
		else:
			print "Memory exceeded in %s space in ints" % self.name
			sys.exit()

	def getNextDouble(self):
		if self.doublesActual + 1 < self.boolsBase:
			nextDouble = self.doublesActual
			self.doublesActual += 1
			return nextDouble
		else:
			print "Memory exceeded in %s space in doubles" % self.name
			sys.exit()

	def getNextBool(self):
		if self.boolsActual + 1 <= self.pointerBase:
			nextBool = self.boolsActual
			self.boolsActual += 1
			return nextBool
		else:
			print "Memory exceeded in %s space in bools" % self.name
			sys.exit()

	def getNextPointer(self):
		if self.pointerActual + 1 <= self.last:
			nextPointer = self.pointerActual
			self.pointerActual += 1
			return nextPointer
		else:
			print "Memory exceeded in %s space in pointer" % self.name
			sys.exit()

	def isPointer(self, address):
		if address >= self.pointerBase and address <= self.last:
			return True
		else:
			return False

	def delLastAssigned(self, typee):
		if typee == 'bool':
			self.boolsActual -= 1
		elif typee == 'double':
			self.doublesActual -= 1
		elif typee == 'int':
			self.intsActual -= 1

	def deleteMemSpace(self):
		self.intsActual = self.intsBase
		self.doublesActual = self.doublesBase
		self.boolsActual = self.boolsBase
		self.pointerActual = self.pointerBase

	def getSpaceMemType(self, address):
		if address >= self.base and address < self.doublesBase:
			return 'int'
		elif address >= self.doublesBase and address < self.boolsBase:
			return 'double'
		elif address >= self.boolsBase and address <= self.pointerBase:
			return 'bool'
		elif address >= self.pointerBase and address <= self.last:
			return 'pointer'

	def printMemSpace(self):
		print "Name:", self.name
		print "Longitude:", self.long
		print "Base ints:", self.intsBase
		print "Act ints:", self.intsActual
		print "Base doubles:", self.doublesBase
		print "Act doubles:", self.doublesActual
		print "Base bools:", self.boolsBase
		print "Act bools:", self.boolsActual
		print "Base pointers:", self.pointerBase
		print "Act pointers:", self.pointerActual
		print "Last direction:", self.last, "\n"


class Memory():

	def __init__(self):
		self.memory = {}
		self.globalMem = MemSpace('global', 100000, 500)
		self.variableMem = MemSpace('variables', self.globalMem.last + 1, 1000)
		self.temporalMem = MemSpace('temporals', self.variableMem.last + 1, 1500)
		self.constantMem = MemSpace('constants', self.temporalMem.last + 1, 1000)
		self.memory['global'] = {}
		self.memory['variable'] = Stack()
		self.memory['variable'].push({})
		self.memory['temporal'] = Stack()
		self.memory['temporal'].push({})
		self.memory['constant'] = {}

	def availGlobal(self, typee):
		nextTemp = None
		if typee == 'bool':
			nextTemp = self.globalMem.getNextBool()
		elif typee == 'double':
			nextTemp = self.globalMem.getNextDouble()
		elif typee == 'int':
			nextTemp = self.globalMem.getNextInt()
		elif typee == 'pointer':
			nextTemp = self.globalMem.getNextPointer()
		return nextTemp

	def availVar(self, typee):
		nextTemp = None
		if typee == 'bool':
			nextTemp = self.variableMem.getNextBool()
		elif typee == 'double':
			nextTemp = self.variableMem.getNextDouble()
		elif typee == 'int':
			nextTemp = self.variableMem.getNextInt()
		elif typee == 'pointer':
			nextTemp = self.variableMem.getNextPointer()
		return nextTemp

	def availTemp(self, typee):
		nextTemp = None
		if typee == 'bool':
			nextTemp = self.temporalMem.getNextBool()
		elif typee == 'double':
			nextTemp = self.temporalMem.getNextDouble()
		elif typee == 'int':
			nextTemp = self.temporalMem.getNextInt()
		elif typee == 'pointer':
			nextTemp = self.temporalMem.getNextPointer()
		return nextTemp

	def availConst(self, typee):
		nextTemp = None
		if typee == 'bool':
			nextTemp = self.constantMem.getNextBool()
		elif typee == 'double':
			nextTemp = self.constantMem.getNextDouble()
		elif typee == 'int':
			nextTemp = self.constantMem.getNextInt()
		elif typee == 'pointer':
			nextTemp = self.constantMem.getNextPointer()
		return nextTemp

	def deleteMems(self):
		self.variableMem.deleteMemSpace()
		self.temporalMem.deleteMemSpace()

	def popMem(self):
		self.memory['variable'].pop()
		self.memory['temporal'].pop()

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

	def getValFromMemWhenAddress(self, dir):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			return self.getValFromMem(self.memory['global'][dir])
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			return self.getValFromMem(self.memory['variable'].peekFromDict(dir))
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			return self.getValFromMem(self.memory['temporal'].peekFromDict(dir))
		elif dir >= self.constantMem.base and dir <= self.constantMem.last:
			return self.getValFromMem(self.memory['constant'][dir])

	def getValFromMemBefore(self, dir):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			return self.memory['global'][dir]
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			return self.memory['variable'].peekSecondFromDict(dir)
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			return self.memory['temporal'].peekSecondFromDict(dir)
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

	def delLastAssignedAddress(self, typee):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			self.globalMem.delLastAssigned(typee)
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			self.variableMem.delLastAssigned(typee)
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			self.temporalMem.delLastAssigned(typee)
		elif dir >= self.constantMem.base and dir <= self.constantMem.last:
			self.constantMem.delLastAssigned(typee)

	def pushToVarStack(self, dirr):
		self.memory['variable'].push(dirr)

	def pushToTempStack(self, dirr):
		self.memory['temporal'].push(dirr)

	def isDir(self, dirr):
		if dir >= self.globalMem.base and dir <= self.globalMem.last:
			return self.globalMem.isPointer(dirr)
		elif dir >= self.variableMem.base and dir <= self.variableMem.last:
			return self.variableMem.isPointer(dirr)
		elif dir >= self.temporalMem.base and dir <= self.temporalMem.last:
			return self.temporalMem.isPointer(dirr)
		elif dir >= self.constantMem.base and dir <= self.constantMem.last:
			return self.constantMem.isPointer(dirr)


	def printMemory(self):
		'''self.globalMem.printMemSpace()
		self.variableMem.printMemSpace()
		self.temporalMem.printMemSpace()
		self.constantMem.printMemSpace()'''
		for key in self.memory:
			if type(self.memory[key]) is dict:
				print key
				print self.memory[key]
			else:
				print key
				self.memory[key].printStack()
			
