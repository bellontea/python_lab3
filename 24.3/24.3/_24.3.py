str = ''
while True:
	word = input()
	if word == '':
		break
	if str != '':
		str += '\n'
	str += word

for index, line in enumerate(str.split('\n')):
	if line.lstrip().startswith('#'):
		print('Line {}: {}'.format(index+1, line.strip().lstrip('#')))
