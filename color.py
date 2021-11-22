for i in range(111):
	if i%8 == 0:
		print()
	print("\x1b[" + str(i) + "m" + str(i) + 'clr\t' + "\x1b[0m", end = "")
print()