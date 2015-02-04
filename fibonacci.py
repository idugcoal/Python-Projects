def fib():
	a = 0
	b = 1
	limit = input("Enter the upper limit: ")

	c = a + b

	print a
	print b

	while c < limit:
		print "number is: " + str(c)
		a = b
		b = c
		c = a + b

fib()
