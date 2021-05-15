def bracket_check(test_string):
	test_string.replace(' ', '')
	count1 = test_string.count('(')
	count2 = test_string.count(')')
	if (count1 == count2):
		print("YES")
	else:
		print("NO")