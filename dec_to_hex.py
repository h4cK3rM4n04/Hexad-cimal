def dectohex (chaine):
	res = ""
	liste = "0123456789ABCDEF"
	if chaine == 0:
		return (chaine)
	while chaine != 0:
		res += liste[chaine%16]
		chaine //= 16
	return res[::-1]
print(dectohex(3247))