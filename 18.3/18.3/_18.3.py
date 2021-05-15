def fyb(i):
	fib1 = 1
	fib2 = 1
	j = 2
	fib_sum = 1
	while j < i:        
		fib_sum = fib2 + fib1
		fib1, fib2 = fib2, fib_sum
		j += 1
	return fib_sum

def golden_ratio(i):
	print(fyb(i + 1) / fyb(i))
