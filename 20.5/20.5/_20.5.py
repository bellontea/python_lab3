def sum_(number):
		x = list(map(int,str(number)))
		return sum(x[:3] ) == sum(x[3:] )
def lucky(ticket):
	return  'Счастливый' if  sum_(ticket) == sum_(lastTicket) else 'Несчастливый'
