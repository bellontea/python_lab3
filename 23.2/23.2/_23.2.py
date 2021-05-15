def find_farthest_orbit(list_of_orbits):
	for i in list_of_orbits:
		if i[0] == i[1]:
			list_of_orbits.remove(i)
	lenght_of_orbits = list(map(lambda a: a[0] * a[1] * 3.14, list_of_orbits))
	return list_of_orbits[lenght_of_orbits.index(max(lenght_of_orbits))]
