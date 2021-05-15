jokes = []

def print_only_new(message):
	if (jokes.count(message) == 0):
		print(message)
		jokes.append(message)