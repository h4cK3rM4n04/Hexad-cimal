#Auteur: Manoa Elie
#Date: Vendredi 25/11/2022
#Heure: 22:18 Pm
#Source d'inspiration: Conversion shadoktodec base 4 sur Jupyter
#===========SCRIPT QUI PERMET DE CONVERTIR UN NOMBRE HEXADECIMAL EN DECIMAL================
def hextodec(chaine):
	liste = "0123456789ABCDEF"
	res = 0
	rang = 0
	for i in reversed(chaine):
		#print(i)
		for j in range(16):
			#print(j)
			if i == liste[j]:
				res += j * 16**rang
				rang += 1
	return res
print(hextodec("CAF"))
print(hextodec("CFF"))