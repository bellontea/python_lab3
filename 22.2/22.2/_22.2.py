def partial_sums(*args):
	sums = [0]
	for x in args:
			sums.append(x + sums[-1])
	return sums