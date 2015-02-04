# 99 bottles of beer on the wall
for i in range(99, 0, -1):
	b = "bottles"
	print "%d %s of beer on the wall" % (i, b)
	print "%d %s of beer" % (i, b)
	print "take one down, pass it around"
	if i - 1 == 1:
		b = "bottle"
	else:
		b = "bottles"
	print "%d %s of beer on the wall\n" % (i - 1, b)