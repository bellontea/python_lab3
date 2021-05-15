def score(zona, cector=0):
	global scoring
	if cector == 0:
		return scoring[zona]
	return score[zona][cector]
