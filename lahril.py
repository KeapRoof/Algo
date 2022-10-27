from ast import While
from ctypes.wintypes import SIZE
from locale import dcgettext
from this import d
from numpy import *

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

def crible(crib):
    n = len(crib)
    c=0
    while c != n:
        crib[c] = True
    crib[0] = False
    if n>= 2:
        crib[1]= False
    cpt = 2
    while cpt < n:
        crib[cpt*2] = False
        cpt = cpt+1
    return crib

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

#fin des tri

def nb_premier(n):
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i = i+1
    return True