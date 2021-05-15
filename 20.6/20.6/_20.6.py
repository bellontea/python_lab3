bets = []

def do_bet(num, bet):
	if (bets.count(num) == 0 and bet != 0):
		print("Ваша ставка в размере %s на лошадь %d принята" %(bet, num))
		bets.append(num)
	else:
		print("Что-то пошло не так, попробуйте еще раз")