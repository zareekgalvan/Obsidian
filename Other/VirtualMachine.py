from Quadruples import *
from Declarations import *
import sys
from Functions import *

class VirtualMachine():
	
	def __init__(self):
		self.quads = []
		self.instructionPointer = 0
		self.jumpStack = Stack()
		self.actualScope = ['main']

	def execute(self, quads):
		self.quads = quads
		
		while self.instructionPointer < Quadruples.cont-1:
			
			quad = self.quads[self.instructionPointer]
			#print 'quad:', quad.number, 'optr:', quad.optr
			# Suma
			if quad.optr == 1:
				if mem.isDir(quad.opLeft):
					left = mem.getValFromMemWhenAddress(quad.opLeft)
				else:
					left = mem.getValFromMem(quad.opLeft)
				if left == None:
					left = mem.getValFromMemBefore(quad.opLeft)

				if mem.isDir(quad.opRight):
					right = mem.getValFromMemWhenAddress(quad.opRight)
				else:
					right = mem.getValFromMem(quad.opRight)

				if left == None:
					print "1.Variables must contain a value before can be used l"
					print quad.opLeft, quad.number
					mem.printMemory()
					sys.exit()
				if right == None:
					print "1.Variables must contain a value before can be used r"
					print right
					mem.printMemory()
					sys.exit()

				self.nextQuad()
				toAssign = left + right
				if mem.isDir(quad.result):
					assign = mem.getValFromMem(quad.result)
				else:
					assign = quad.result
				print 'assign:', toAssign, 'in:', mem.isDir(quad.result)
				mem.putValInMem(assign, toAssign)
			# Resta
			elif quad.optr == 2:
				
				if mem.isDir(quad.opLeft):
					left = mem.getValFromMemWhenAddress(quad.opLeft)
				else:
					left = mem.getValFromMem(quad.opLeft)
				if left == None:
					left = mem.getValFromMemBefore(quad.opLeft)

				if mem.isDir(quad.opRight):
					right = mem.getValFromMemWhenAddress(quad.opRight)
				else:
					right = mem.getValFromMem(quad.opRight)

				if left == None:
					print "2.Variables must contain a value before can be used l"
					print left, quad.number
					mem.printMemory()
					sys.exit()
				if right == None:
					print "2.Variables must contain a value before can be used r"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left - right
				if mem.isDir(quad.result):
					assign = mem.getValFromMem(quad.result)
				else:
					assign = quad.result
				mem.putValInMem(assign, toAssign)
			# Multiplicacion
			elif quad.optr == 3:

				if mem.isDir(quad.opLeft):
					left = mem.getValFromMemWhenAddress(quad.opLeft)
				else:
					left = mem.getValFromMem(quad.opLeft)
				if left == None:
					left = mem.getValFromMemBefore(quad.opLeft)

				if mem.isDir(quad.opRight):
					right = mem.getValFromMemWhenAddress(quad.opRight)
				else:
					right = mem.getValFromMem(quad.opRight)

				if left == None:
					print "3.Variables must contain a value before can be used l"
					print left, quad.opLeft
					mem.printMemory()
					sys.exit()
				if right == None:
					print "3.Variables must contain a value before can be used r"
					print right, quad.opRight
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left * right
				if mem.isDir(quad.result):
					assign = mem.getValFromMem(quad.result)
				else:
					assign = quad.result

				mem.putValInMem(assign, toAssign)
			# Division
			elif quad.optr == 4:
				
				if mem.isDir(quad.opLeft):
					left = mem.getValFromMemWhenAddress(quad.opLeft)
				else:
					left = mem.getValFromMem(quad.opLeft)
				if left == None:
					left = mem.getValFromMemBefore(quad.opLeft)

				if mem.isDir(quad.opRight):
					right = mem.getValFromMemWhenAddress(quad.opRight)
				else:
					right = mem.getValFromMem(quad.opRight)

				if left == None:
					print "4.Variables must contain a value before can be used"
					print left
					mem.printMemory()
					sys.exit()
				if right == None:
					print "4.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left / right
				if mem.isDir(quad.result):
					assign = mem.getValFromMem(quad.result)
				else:
					assign = quad.result
				mem.putValInMem(assign, toAssign)
			# Mod
			elif quad.optr == 5:
				
				if mem.isDir(quad.opLeft):
					left = mem.getValFromMemWhenAddress(quad.opLeft)
				else:
					left = mem.getValFromMem(quad.opLeft)
				if left == None:
					left = mem.getValFromMemBefore(quad.opLeft)

				if mem.isDir(quad.opRight):
					right = mem.getValFromMemWhenAddress(quad.opRight)
				else:
					right = mem.getValFromMem(quad.opRight)

				if left == None:
					print "5.Variables must contain a value before can be used"
					print left
					mem.printMemory()
					sys.exit()
				if right == None:
					print "5.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left % right
				if mem.isDir(quad.result):
					assign = mem.getValFromMem(quad.result)
				else:
					assign = quad.result
				mem.putValInMem(assign, toAssign)
			# Equals
			elif quad.optr == 6:

				if mem.isDir(quad.opLeft):
					toAssign = mem.getValFromMemWhenAddress(quad.opLeft)
				else:
					toAssign = mem.getValFromMem(quad.opLeft)

				if toAssign == None:
					print "6.No value for address %s from quad %s" % (quad.opLeft, quad.number)
					mem.printMemory()
					sys.exit()
			
				if mem.isDir(quad.result):
					assign = mem.getValFromMem(quad.result)
				else:
					assign = quad.result

				mem.putValInMem(assign, toAssign)
				self.nextQuad()
			# Equal equals	
			elif quad.optr == 7:
				
				if mem.isDir(quad.opLeft):
					left = mem.getValFromMemWhenAddress(quad.opLeft)
				else:
					left = mem.getValFromMem(quad.opLeft)
				if left == None:
					left = mem.getValFromMemBefore(quad.opLeft)

				if mem.isDir(quad.opRight):
					right = mem.getValFromMemWhenAddress(quad.opRight)
				else:
					right = mem.getValFromMem(quad.opRight)

				if left == None:
					print "7.Variables must contain a value before can be used l"
					print left, mem.getValFromMem(quad.opLeft)
					#mem.printMemory()
					sys.exit()
				if right == None:
					print "7.Variables must contain a value before can be used"
					print right, mem.getValFromMem(quad.opRight)
					#mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left == right
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Different
			elif quad.optr == 8:
				
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "8.Variables must contain a value before can be used"
					print left
					mem.printMemory()
					sys.exit()
				if right == None:
					print "8.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left != right
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Less than
			elif quad.optr == 9:
				
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "9.Variables must contain a value before can be used l"
					print quad.opLeft, quad.number
					mem.printMemory()
					sys.exit()
				if right == None:
					print "9.Variables must contain a value before can be used r"
					print quad.opRight, quad.number
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left < right
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Greater than
			elif quad.optr == 10:
				
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "10.Variables must contain a value before can be used"
					print left
					mem.printMemory()
					sys.exit()
				if right == None:
					print "10.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left > right
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Less or equal than
			elif quad.optr == 11:
				
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMemBefore(quad.opRight)
				if left == None:
					print "11.Variables must contain a value before can be used"
					print left, quad.number
					mem.printMemory()
					sys.exit()
				if right == None:
					print "11.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left <= right
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Greater or equal than
			elif quad.optr == 12:
				
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "12.Variables must contain a value before can be used"
					print left
					mem.printMemory()
					sys.exit()
				if right == None:
					print "12.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left >= right
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# And
			elif quad.optr == 13:
				
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "13.Variables must contain a value before can be used"
					print left
					mem.printMemory()
					sys.exit()
				if right == None:
					print "13.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left == 'true' and right == 'true'
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Or
			elif quad.optr == 14:
				
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "14.Variables must contain a value before can be used"
					print left
					mem.printMemory()
					sys.exit()
				if right == None:
					print "14.Variables must contain a value before can be used"
					print right
					mem.printMemory()
					sys.exit()
				self.nextQuad()
				toAssign = left == 'true' or right == 'true'
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Read
			elif quad.optr == 15:
				
				inp = raw_input(">")
				self.nextQuad()
				if isInt(inp):
					if mem.getTypeFromMem(quad.result) == 'int':
						mem.putValInMem(quad.result, int(inp))
					else:
						print "Type mismatch in assignation from read"
						sys.exit()
				elif isDouble(inp):
					if mem.getTypeFromMem(quad.result) == 'double':
						mem.putValInMem(quad.result, float(inp))
					else:
						print "Type mismatch in assignation from read"
						sys.exit()
				elif inp == 'true' or inp == 'false':
					if mem.getTypeFromMem(quad.result) == 'bool':
						mem.putValInMem(quad.result, inp)
					else:
						print "Type mismatch in assignation from read"
						sys.exit()
				else:
					print "String not supported in this language"
					sys.exit() 
			# Write
			elif quad.optr == 16:
				
				self.nextQuad()
				toPrint = mem.getValFromMem(quad.result)
				if toPrint == None:
					print "Cant print variable because it has no value"
					mem.printMemory()
					sys.exit()

				toPrint = quad.result
				print "<<", mem.getValFromMem(toPrint)
			# Return
			elif quad.optr == 17:
				
				toAssign = mem.getValFromMem(quad.result)
				address = varTable['global'][self.getScope()]['address']
				mem.putValInMem(address, toAssign)
				#print address, toAssign
				self.nextQuad()
			# Endproc
			elif quad.optr == 18:
				
				self.jump(self.jumpStack.peek())
				self.jumpStack.pop()
				self.actualScope.pop()
				mem.popMem()
			# Gosub
			elif quad.optr == 19:
				
				jumpTo = quad.result
				self.jump(jumpTo)
				self.jumpStack.push(quad.number+1)
				push_false_bottom()
			# Era
			elif quad.optr == 20:

				mem.pushToVarStack(getVirtualVariblesFromVarTable(quad.result))
				mem.pushToTempStack(getVirtualTemporalsFromVarTable(quad.result))
				self.actualScope.append(quad.result)
				self.nextQuad()
			# GotoF
			elif quad.optr == 21:
				
				left = mem.getValFromMem(quad.opLeft)
				if left == None:
					print "21.Variables must contain a value before can be used"
					sys.exit()
				self.nextQuad()
				if left == 'false':
					self.jump(quad.result)
			# GotoT
			elif quad.optr == 22:
				print "GotoT not suported in this language"
			# Goto
			elif quad.optr == 23:
				
				self.jump(quad.result)
			# End
			elif quad.optr == 24:
				
				return
			# Param
			elif quad.optr == 25:
				
				address = tryGetAddressFromParamNo(self.getScope(), quad.opRight)
				toAssign = mem.getValFromMem(quad.opLeft)
				if toAssign == None:
					toAssign = mem.getValFromMemBefore(quad.opLeft)
				mem.putValInMem(address, toAssign)
				#print mem.getValFromMem(address)
				#mem.printMemory()
				self.nextQuad()
			# Ver
			elif quad.optr == 26:
				ver = mem.getValFromMem(quad.opLeft)
				if ver == None:
					print "26.Variables must contain a value before can be used"
					sys.exit()
				if ver >= quad.opRight and ver <= quad.result:
					self.nextQuad()
				else:
					print "Array out of bounds with value %s" % ver
					sys.exit()
			# ERROR		
			else:
				print 'unrecognized optr %s' % quad.optr
				self.nextQuad()

	def jump(self, quadNo):
		self.instructionPointer = quadNo - 1

	def nextQuad(self):
		self.instructionPointer += 1

	def getScope(self):
		return self.actualScope[len(self.actualScope)-1]