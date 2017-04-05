class VirtualMachine(quads):
	for x in quads:
		if x.optr == 1:
			# +
		elif x.optr == 2:
			# -
		elif x.optr == 3:
			# *
		elif x.optr == 4:
			# /
		elif x.optr == 5:
			# %
		elif x.optr == 6:
			# =
		elif x.optr == 7:
			# ==
		elif x.optr == 8:
			# !=
		elif x.optr == 9:
			# <
		elif x.optr == 10:
			# >
		elif x.optr == 11:
			# <=
		elif x.optr == 12:
			# >=
		elif x.optr == 13:
			# &&
		elif x.optr == 14:
			# ||
		elif x.optr == 15:
			# read
		elif x.optr == 16:
			# write
		elif x.optr == 17:
			# return
		elif x.optr == 18:
			# Endproc
		elif x.optr == 19:
			# gosub
		elif x.optr == 20:
			# era
		elif x.optr == 21:
			# GotoF
		elif x.optr == 22:
			# GotoT
		elif x.optr == 23:
			# Goto
		elif x.optr == 24:
			# END
		elif x.optr == 25:
			# param