from Quadruples import *
from Declarations import *

class VirtualMachine():
	
	def __init__(self):
		self.quads = []
		self.instructionPointer = 0
		self.jumpStack = Stack()

	def execute(self, quads):
		self.quads = quads
		while self.instructionPointer < Quadruples.cont-1:
			quad = self.quads[self.instructionPointer]
			if quad.optr == 1:
				# +
				print "suma"
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				self.instructionPointer += 1
				print left, right
			elif quad.optr == 2:
				# -
				print "resta"
				left = mem.getValFromMem(quad.opLeft)
				right = mem.getValFromMem(quad.opRight)
				self.instructionPointer += 1
				print ">>", left, right
			elif quad.optr == 3:
				# *
				self.instructionPointer += 1
				print "mult"
			elif quad.optr == 4:
				# /
				self.instructionPointer += 1
				print "div"
			elif quad.optr == 5:
				# %
				self.instructionPointer += 1
				print "mod"
			elif quad.optr == 6:
				# =
				self.instructionPointer += 1
				print "equal"
			elif quad.optr == 7:
				# ==
				self.instructionPointer += 1
				print "equal equals"
			elif quad.optr == 8:
				# !=
				self.instructionPointer += 1
				print "dif"
			elif quad.optr == 9:
				# <
				self.instructionPointer += 1
				print "less"
			elif quad.optr == 10:
				# >
				self.instructionPointer += 1
				print "greater"
			elif quad.optr == 11:
				# <=
				self.instructionPointer += 1
				print "lesser than"
			elif quad.optr == 12:
				# >=
				self.instructionPointer += 1
				print "greater than"
			elif quad.optr == 13:
				# &&
				self.instructionPointer += 1
				print "and"
			elif quad.optr == 14:
				# ||
				self.instructionPointer += 1
				print "or"
			elif quad.optr == 15:
				# read
				self.instructionPointer += 1
				print "read"
			elif quad.optr == 16:
				# write
				self.instructionPointer += 1
				print "write"
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
				print "gotof"
				self.instructionPointer += 1
			elif quad.optr == 22:
				# GotoT
				print "gotot"
			elif quad.optr == 23:
				# Goto
				print "goto"
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