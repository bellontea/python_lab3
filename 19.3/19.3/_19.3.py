def roots_of_quadratic_equation(a,b,c):
	if a==0 and b==0 and c==0:
		return ['all']
	elif a == 0 and b == 0:
		return []
	elif a==0:
		return [(c*(-1))/b]
	elif b==0:
		return [((-1*b)/a) ** 0.5]
	elif  c==0:
		return[0, (-1*b)/a]
	else:
		q = b**2
		w = -4*a*c
		D = q+w
		if D<0:
			return[]
		elif D== 0:
			return[(-1*b)/(2*a)]
		else:
			D **= 0.5
			return[int(((-1*b)-D)/(2*a)), ((-1*b)+D)/(2*a)]
