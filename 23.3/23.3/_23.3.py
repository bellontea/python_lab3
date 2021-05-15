def Puh(line):
	lines = line.split()
	for i in lines:
		if sum(list(map((lambda a: int('уеыаоэяию'.find(a) != -1)), i))) % 2 == 1:
			return "Пам парам"
	return "Парам пам-пам"

line = input().lower()
print(Puh(line));
