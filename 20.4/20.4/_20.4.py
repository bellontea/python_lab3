def hello(temp):
	print("Здравствуйте,", temp + '!', "Вашу карту ищут...")

def search_card(temp):
	global base
	if temp in base:
		print("Ваша карта с номером",base.index(temp)+1,"найдена")
	else:
		print("Ваша карта не найдена")
