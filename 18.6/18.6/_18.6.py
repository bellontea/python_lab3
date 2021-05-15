def line(s, t):
	k, b = s.split('x')
	x, y = t.split(';')
	k, b, x, y = int(k), int(b), int(x), int(y)
	y2 = k * x + b
	if (y2 == y):
		print("True")
	else:
		print("False")
