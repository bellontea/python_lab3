def swap(first, second):
	temp = []
	temp.extend(first)
	first.clear()
	first.extend(second)
	second.clear()
	second.extend(temp)
	temp.clear()
