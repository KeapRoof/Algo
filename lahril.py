from numpy import *
#test

def min(a,b,c):
    if a < b and a < c:
        return a
    else:
        if b < c:
            return b
        else:
            return c

def max(a,b,c):
    if a > b and a > c:
        return a
    else:
        if b > c:
            return b
        else:
            return c

def exo(a,b,c):
    x = min(a,b,c)
    y = max(a,b,c)
    d = x**y
    return d

def titi(a,b):
    n = tutu(a+b,a*2)
    c=n-a
    return c

def tutu(a,b):
    if a < b:
        c=a
    else:
        c=b
    return c

def toto(a):
    n = 4
    n = titi(a*2,n*a)
    b=3*n-2
    return b

def factorielle(n):
   if n == 0:
      return 1
   else:
      F = 1
      for k in range(2,n+1):
         F = F * k
      return F

def sommefacto(x):
    c = 0
    sf = 0
    while c < x:
        sf = sf+factorielle(c)
        c = c+1
    return sf

def sommetab(tab):
    c = 0
    n = len(tab)
    while c < n:
        som = tab[c] + som
        c = c+1 
    return som

def moytab(tab):
    c = 0
    n = len(tab)
    while c < n:
        moy = tab[c] + moy
        c = c+1
    moy = moy/n
    return moy

def moytab1(tab):
    moyenne = sommetab(tab)/len(tab)
    return moyenne

def occu(tab,e):
    i = 0
    nb = 0
    n = len(tab)
    while i < n:
        if tab[i] == e:
            nb = nb + 1
        i = i+1
    return nb
        
def palindrome(tab):
    i=0
    n=len(tab)
    mid=n//2
    pal=True
    while i < n:
        if tab[i]!=tab[-i]:
            pal=False
        i=i+1
    return pal

def nbOcc(tab,e):
    nb=0
    i=0
    while i <= len(tab):
        if e==tab[i]:
            nb=nb+1
        i=i+1
    return nb

def fibonacci_tab(tab):
    i=1
    n = len(tab)
    while i < n:
        tab[i]=tab[i-2]+tab[i-1]
        i = i+1
    return tab

def inverse(tab):
    n = len(tab)
    i = 0
    while i < n//2:
        temp = tab[i]
        tab[i] = tab[n-1-i]
        tab[n-1-i] = temp
        i = i+1
    return tab


def recherche_dicho(tab,e):
    n = len(tab)
    i = 0
    temp = tab
    while i < n//2:
        temp = n//2
        if tab[n//2] == e:
            return n//2
        else:
            if tab[n//2] > e:
                temp = tab[n//2:]
                n = len(temp)
            else:
                temp = tab[:n//2]
                n = len(temp)
 
def min(tab):
    min = tab[0]
    n = len(tab)
    i = 0
    while i<n:
        if tab[i]< min:
            min = tab[i]
        i = i+1
    return min

# Debut des tri
def tri_selection(tab):
    n = len(tab)
    i = 0
    while i < n:
        j = i+1
        while j < n:
            if tab[i] > tab[j]:
                temp = tab[i]
                tab[i] = tab[j]
                tab[j] = temp
            j = j+1
        i = i+1
    return tab

def tri_insertion(tab):
    n = len(tab)
    i = 1
    while i < n:
        j = i
        while j > 0 and tab[j-1] > tab[j]:
            temp = tab[j]
            tab[j] = tab[j-1]
            tab[j-1] = temp
            j = j-1
        i = i+1
    return tab

def tri_bulle(tab):
    n = len(tab)
    i = 0
    while i < n:
        j = 0
        while j < n-1:
            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp
            j = j+1
        i = i+1
    return tab
#Nombre premier
def nb_premier(n):
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i = i+1
    return True
#jeu du juste prix
def juste_prix():
    import random
    n = random.randint(1,100)
    i = 0
    while i < 5:
        x = int(input("Entrez un nombre"))
        if x == n:
            print("Bravo")
            return True
        else:
            if x < n:
                print("Plus grand")
            else:
                print("Plus petit")
        i = i+1
    print("Perdu")
    return False

#crible d'Erathostene

def crible(n):
    tab = [True]*n
    tab[0] = False
    tab[1] = False
    i = 2
    while i < n:
        if tab[i] == True:
            j = 2
            while i*j < n:
                tab[i*j] = False
                j = j+1
        i = i+1
    return tab

def nb_premier_crible(n):
    tab = crible(n)
    i = 0
    nb = 0
    while i < n:
        if tab[i] == True:
            nb = nb+1
        i = i+1
    return nb

#tri selection
def tri_selection(tab):
    n = len(tab)
    i = 0
    while i < n:
        j = i+1
        while j < n:
            if tab[i] > tab[j]:
                temp = tab[i]
                tab[i] = tab[j]
                tab[j] = temp
            j = j+1
        i = i+1
    return tab

def fibonacci_rec(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)

def palindrome_rec(tab):
    if len(tab) == 0 or len(tab) == 1:
        return True
    else:
        if tab[0] == tab[-1]:
            return palindrome_rec(tab[1:-1])
        else:
            return False

def recherche_dicho_rec(tab):
    if len(tab) == 0:
        return False
    else:
        if tab[len(tab)//2] == e:
            return True
        else:
            if tab[len(tab)//2] > e:
                return recherche_dicho_rec(tab[len(tab)//2:])
            else:
                return recherche_dicho_rec(tab[:len(tab)//2])

def quotient():
    print("Entrez le dividende")
    a = input()
    print("Entrez le diviseur")
    b = input()
    if b == 0:
        print("Le diviseur est nul !")
        return 1
    if b != 0 and (a < 0 and b < 0):
        print("Un des deux nombre est negatif")    
        return 2
    else:
        q = a / b
        print("Le quotient de ",a,"par",b,"est",q)
        return 0
