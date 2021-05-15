str = ''
while True:
	word = input()
	if word == '':
		break
	if str != '':
		str += '\n'
	str += word

print(any(not all(map(int,x.split())) for x in str.split('\n')))
