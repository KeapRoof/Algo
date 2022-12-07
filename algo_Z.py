from numpy import *


def algo_b(tab : [int], g: int, d: int) -> None:
	"""
	pré-condition: 
	post-condition: ?
	"""
	tmp = zeros(d-g, int)
	i=0
	while i < len(tmp):
		tmp[i] = tab[g+i]
		i += 1
	m = (len(tmp)+1)//2
	c1 = 0
	c2 = m
	i = 0
	while i < len(tmp):
		if c2 >= len(tmp) or (c1 < m and tmp[c1] < tmp[c2]):
			tab[g+i] = tmp[c1]
			c1 += 1
		else:
			tab[g+i] = tmp[c2]
			c2 += 1
		i += 1

		
def algo_a(tab: [int], g: int, d: int) -> None:
	"""
	pré-condition: 
	post-condition: ?
	"""
	if d-g > 1:
		m = (d+g+1)//2
		algo_a(tab, g, m)
		algo_a(tab, m, d)
		algo_b(tab, g, d)
	
	
	
def algo_main(tab : [int]) -> None:
	"""
	pré-condition : 
	post-condition : trie tab par ordre croissant
	"""
	algo_a(tab, 0, len(tab))
		
		
