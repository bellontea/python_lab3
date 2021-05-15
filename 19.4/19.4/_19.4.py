def palindrome(s):
	foo = str(s)
	if foo[::-1] == foo:
		return "Полиндром"
	return "Не полиндром"
