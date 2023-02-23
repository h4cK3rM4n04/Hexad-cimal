#Auteur: Manoa Elie
#Date: Dimanche/18/12/2022
#Heure: 18:52
#Source d'inspiration: Conversion shadoktodec base 4 sur Jupyter
def base_36_to_dec(chaine):
	liste = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	res = 0
	rang = 0
	for i in reversed(chaine):
		for j in range(36):
			#print(j)
			if i == liste[j]:
				res += j * 36**rang
				rang += 1
	return res
print(base_36_to_dec("LOGIPERISURVOL"))