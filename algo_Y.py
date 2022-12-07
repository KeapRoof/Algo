from numpy import *
from random import *
	
def algo_main(tab) -> None:
	"""
	pré-condition : 
	post-condition : trie tab par ordre croissant
	"""
	d = 0
	f = len(tab)-1
	end = False
	while end == False:
		end = True
		i=0
		while i < f:
			if tab[i] > tab[i+1] :
				tmp = tab[i]
				tab[i]=tab[i+1]
				tab[i+1] = tmp
				end = False
			i += 1
		f -= 1
		i=f
		while i > d:
			if tab[i-1] > tab[i] :
				tmp = tab[i]
				tab[i]=tab[i-1]
				tab[i-1] = tmp
				end = False
			i -= 1
		d += 1

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


for loop in range(1000):
	tab = tab_alea(10)	
	algo_main(tab)
	if est_trie(tab) == False:
		print("erreur")
		break
	elif est_trie(tab) == True:
		print("ok")
	