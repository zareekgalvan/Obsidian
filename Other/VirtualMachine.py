class VirtualMachine():
	
	def __init__(self):
		self.quads = []
		self.instructionPointer = 1

	def execute(self, quads):
		self.quads = quads
		for x in self.quads:
			if x.optr == 1:
				# +
				print "suma"
			elif x.optr == 2:
				# -
				print "resta"
			elif x.optr == 3:
				# *
				print "mult"
			elif x.optr == 4:
				# /
				print "div"
			elif x.optr == 5:
				# %
				print "mod"
			elif x.optr == 6:
				# =
				print "equal"
			elif x.optr == 7:
				# ==
				print "equal equals"
			elif x.optr == 8:
				# !=
				print "dif"
			elif x.optr == 9:
				# <
				print "less"
			elif x.optr == 10:
				# >
				print "greater"
			elif x.optr == 11:
				# <=
				print "lesser than"
			elif x.optr == 12:
				# >=
				print "greater than"
			elif x.optr == 13:
				# &&
				print "and"
			elif x.optr == 14:
				# ||
				print "or"
			elif x.optr == 15:
				# read
				print "read"
			elif x.optr == 16:
				# write
				print "write"
			elif x.optr == 17:
				# return
				print "return"
			elif x.optr == 18:
				# Endproc
				print "endproc"
			elif x.optr == 19:
				# gosub
				print "gosub"
			elif x.optr == 20:
				# era
				print "era"
			elif x.optr == 21:
				# GotoF
				print "gotof"
			elif x.optr == 22:
				# GotoT
				print "gotot"
			elif x.optr == 23:
				# Goto
				print "goto"
			elif x.optr == 24:
				# END
				print "END"
			elif x.optr == 25:
				# param
				print "param"