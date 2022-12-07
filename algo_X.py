from numpy import *
from random import randint
	
def algo_main(tab) -> None:
	"""
	pré-condition : 
	post-condition : trie tab par ordre croissant
	"""
	i=1
	while i < len(tab):
		j=i-1
		tmp = tab[i]
		while tmp < tab[j] and j >= 0:
			tab[j+1] = tab[j]
			tab[i] = tmp
		j = j - 1
		i += 1
	return tab

# est trie

def est_trie(tab) -> bool:
	i=0
	while i < len(tab)-1:
		if tab[i] > tab[i+1]:
			return False
		i += 1
	return True


# tableau aleatoire

def tab_alea(n):	
	tab = []
	i=0
	while i < n:
		tab.append(randint(0, 100))
		i += 1
	return tab

tab = tab_alea(10)
print(tab)
algo_main(tab)
print(tab)

"""
for loop in range(1000):
	tab = tab_alea(10)	
	algo_main(tab)
	if est_trie(tab) == False:
		print("erreur")
		break
	elif est_trie(tab) == True:
		print("ok")
	
"""