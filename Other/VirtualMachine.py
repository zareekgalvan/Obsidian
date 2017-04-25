from Quadruples import *
from Declarations import *
import sys
from Functions import *

class VirtualMachine():
	
	def __init__(self):
		self.quads = []
		self.instructionPointer = 0
		self.jumpStack = Stack()

	def execute(self, quads):
		self.quads = quads
		
		while self.instructionPointer < Quadruples.cont-1:
			
			quad = self.quads[self.instructionPointer]
			
			# Suma
			if quad.optr == 1:
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				toAssign = left + right
				mem.putValInMem(quad.result, toAssign)
			# Resta
			elif quad.optr == 2:
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				toAssign = left - right
				mem.putValInMem(quad.result, toAssign)
			# Multiplicacion
			elif quad.optr == 3:
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				toAssign = left * right
				mem.putValInMem(quad.result, toAssign)
			# Division
			elif quad.optr == 4:
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				toAssign = left / right
				mem.putValInMem(quad.result, toAssign)
			# Mod
			elif quad.optr == 5:
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				toAssign = left % right
				mem.putValInMem(quad.result, toAssign)
			# Equals
			elif quad.optr == 6:
				toAssign = mem.getValFromMem(quad.opLeft)
				if toAssign == None:
					print "No value for %s address" % getID(quad.opLeft)
					sys.exit()
				mem.putValInMem(quad.result, toAssign)
				self.instructionPointer += 1
			# Equal equals	
			elif quad.optr == 7:
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
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
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
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
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
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
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				toAssign = left > right
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Less or equal than
			elif quad.optr == 11:
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
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
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
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
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
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
					print "Variables must contain a value before can be used"
					sys.exit()
				if right == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				toAssign = left == 'true' or right == 'true'
				if toAssign:
					mem.putValInMem(quad.result, 'true')
				else:
					mem.putValInMem(quad.result, 'false')
			# Read
			elif quad.optr == 15:
				inp = raw_input(">")
				self.instructionPointer += 1
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
				self.instructionPointer += 1
				print mem.getValFromMem(quad.result)
			elif quad.optr == 17:
				# return
				self.instructionPointer += 1
				print "return"
			elif quad.optr == 18:
				# Endproc
				print "endproc"
				self.jump(self.jumpStack.peek())
				self.jumpStack.pop()
			elif quad.optr == 19:
				# gosub
				jumpTo = quad.result
				self.jump(jumpTo)
				self.jumpStack.push(quad.number+1)
				print "gosub"
			elif quad.optr == 20:
				# era
				print "era"
				self.instructionPointer += 1
			elif quad.optr == 21:
				# GotoF
				left = mem.getValFromMem(quad.opLeft)
				if left == None:
					print "Variables must contain a value before can be used"
					sys.exit()
				self.instructionPointer += 1
				if left == 'false':
					self.jump(quad.result)
			elif quad.optr == 22:
				# GotoT
				print "GotoT not suported in this language"
			elif quad.optr == 23:
				# Goto
				self.jump(quad.result)
			elif quad.optr == 24:
				# END
				
				return
			elif quad.optr == 25:
				# param
				print "param"
				self.instructionPointer += 1

	def jump(self, quadNo):
		self.instructionPointer = quadNo - 1