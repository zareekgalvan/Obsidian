from Quadruples import *

class VirtualMachine():
	
	def __init__(self):
		self.quads = []
		self.instructionPointer = 1

	def execute(self, quads):
		self.quads = quads
		while self.instructionPointer < Quadruples.cont-1:
			if self.quads[self.instructionPointer].optr == 1:
				# +
				print "suma"

			elif self.quads[self.instructionPointer].optr == 2:
				# -
				print "resta"
			elif self.quads[self.instructionPointer].optr == 3:
				# *
				print "mult"
			elif self.quads[self.instructionPointer].optr == 4:
				# /
				print "div"
			elif self.quads[self.instructionPointer].optr == 5:
				# %
				print "mod"
			elif self.quads[self.instructionPointer].optr == 6:
				# =
				print "equal"
			elif self.quads[self.instructionPointer].optr == 7:
				# ==
				print "equal equals"
			elif self.quads[self.instructionPointer].optr == 8:
				# !=
				print "dif"
			elif self.quads[self.instructionPointer].optr == 9:
				# <
				print "less"
			elif self.quads[self.instructionPointer].optr == 10:
				# >
				print "greater"
			elif self.quads[self.instructionPointer].optr == 11:
				# <=
				print "lesser than"
			elif self.quads[self.instructionPointer].optr == 12:
				# >=
				print "greater than"
			elif self.quads[self.instructionPointer].optr == 13:
				# &&
				print "and"
			elif self.quads[self.instructionPointer].optr == 14:
				# ||
				print "or"
			elif self.quads[self.instructionPointer].optr == 15:
				# read
				print "read"
			elif self.quads[self.instructionPointer].optr == 16:
				# write
				print "write"
			elif self.quads[self.instructionPointer].optr == 17:
				# return
				print "return"
			elif self.quads[self.instructionPointer].optr == 18:
				# Endproc
				print "endproc"
			elif self.quads[self.instructionPointer].optr == 19:
				# gosub
				print "gosub"
			elif self.quads[self.instructionPointer].optr == 20:
				# era
				print "era"
			elif self.quads[self.instructionPointer].optr == 21:
				# GotoF
				print "gotof"
			elif self.quads[self.instructionPointer].optr == 22:
				# GotoT
				print "gotot"
			elif self.quads[self.instructionPointer].optr == 23:
				# Goto
				print "goto"
			elif self.quads[self.instructionPointer].optr == 24:
				# END
				print "END"
			elif self.quads[self.instructionPointer].optr == 25:
				# param
				print "param"
			self.instructionPointer += 1