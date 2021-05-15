def ask_password():
	i = 0
	password = "password"
	while True:
		s = input()
		if (i == 3):
			continue
		i += 1
		if s == password:
			print("Пароль принят")
			i += 3
		elif i == 3:
			print("В доступе отказано")
