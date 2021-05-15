def equation(xy1, xy2):
	x1 = int(xy1.split(";")[0])
	y1 = int(xy1.split(";")[1])
	x2 = int(xy2.split(";")[0])
	y2 = int(xy2.split(";")[1])
	k = 0
	if (x1 - x2) == 0:
		print(float(x1))
		return
	if (y1 - y2) == 0:
		print(float(y1))
		return
	k = (y1 - y2) / (x1 - x2)
	b = y2 - k * x2
	print(k, b)