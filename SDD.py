class Maillon:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Liste_chainee:
    def __init__(self):
        self.head = None

    def SizeListe(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def search(self,val):
        temp = self.head
        while temp != None:
            if self.data == val:
                return True,temp
            else:
                temp = temp.next
        return False,None

    def nb_occ(self,val):
        temp = self.head
        count = 0
        while temp != None:
            if temp.data == val:
                count += 1
            temp = temp.next
        return count

    def somme(self):
        temp = self.head
        somme = 0
        while temp != None:
            somme += temp.data
            temp = temp.next
        return somme

    def separer(self):
        half = self.SizeListe() / 2
        head1 = self.head
        temp = self.head
        i=0
        while temp != None:
            if i == half:
                return head1, temp
            temp = temp.next
            i += 1
    
    def inseret_fin(self,val):
        temp = self.head
        while temp != None:
            if temp.next == None:
                temp.data = val
            temp = temp.next
        return temp

    def insert_deb(self,val):
        maillon = Maillon(val)
        maillon.next = self.head
        self.head = maillon

    def insert_juste_apres(self,val,ptr):
        maillon = Maillon(val)
        temp = self.head
        while temp != ptr:
            temp = temp.next
        maillon.next = temp.next
        temp.next = maillon
        return self

    def insert(self,val):
        temp = self.head
        precedent = self.head
        if self.head.val > val:
            self.insert_deb
        while temp != None:
            if temp.data <= val:
                precedent = temp
                temp = temp.next
            else:
                self.insert_juste_apres(val,precedent)
        return self

    def duplique(self,val):
        temp = self.head
        while temp != None:
            if temp.data == val:
                self.insert_juste_apres(val,temp)
            temp = temp.next
        return self

    def suppression(self,val):
        temp = self.head
        precedent = self.head
        while temp != None:
            if temp.data == val:
                precedent.next = temp.next
                del temp
                return True,self.head
            precedent = temp
            temp = temp.next
        return False,self.head

    def fusion(self,listetemp):
        temp1 = self.head
        temp2 = listetemp.head
        res = Liste_chainee()
        if self.taille == listetemp.taille:
            while temp1 != None or temp2 != None:
                if temp2.data > temp1.data:
                    res.insert(temp1.data)
                    temp1 = temp1.next
                    if temp1 == None:
                        while temp2 != None:
                            res.inseret_fin(temp2.data)
                            temp2 = temp2.data
                else:
                    res.insert(temp2.data)
                    temp2 = temp2.next
                    if temp2 == None:
                        while temp1 != None:
                            res.inseret_fin(temp1.data)
                            temp1 = temp1.data
        return res

    def fision(self):
        paire = Liste_chainee()
        impaire = Liste_chainee()
        temp = self.head
        while temp != None:
            if temp.data % 2 == 0:
                paire.inseret_fin(temp.data)
                temp = temp.next
            else:
                impaire.insert_fin(temp.data)
                temp = temp.next
        return paire,impaire


class biMaillon:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.past = None

class Bliste:
    def __init__(self):
        self.head = None

    def sizebliste(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count
    
    def insert_deb(self,val):
        maillon = Maillon(val)
        maillon.next = self.head
        self.head.past = maillon
        self.head = maillon

    def insert_just_apres2(self,val,ptr):
        maillon = biMaillon(val)
        temp = ptr
        maillon.next = temp.next
        temp.next.past = maillon
        temp.next = maillon
        maillon.past = temp
        return self

    def insert(self,val):
        temp = self.head
        value = False
        if self.head.val > val:
            self.insert_deb(val)
            value = True
        while temp != None:
            if temp.data <= val:
                temp = temp.next
            else:
                self.insert_just_apres2(val,temp.past)
                value = True
        return self,value
    
    def insert_juste_apres(self,val,ptr):
        maillon = biMaillon(val)
        temp = self.head
        while temp != ptr:
            temp = temp.next
        maillon.next = temp.next
        temp.next.past = maillon
        temp.next = maillon
        maillon.past = temp
        return self
    
    def insert_just_apres2(self,val,ptr):
        maillon = biMaillon(val)
        temp = ptr
        maillon.next = temp.next
        temp.next.past = maillon
        temp.next = maillon
        maillon.past = temp
        return self
    
    def suppression(self,val):
        val = False
        temp = self.head
        if temp.data == val:
            self.head = temp.next
            temp.next.past = None
            del temp
            return self,True
        while temp.data != val:
            temp = temp.next
        temp.past.next = temp.next
        if temp.next.past != None:
            temp.next.past = temp.past
        del temp
        value = True
        return self,value

    class Listecirculaire():

        def __init__(self):
            self.start = None

    # Insertion d'un élément dans la liste circulaire d'ordre croissant avec le BiMaillon

        def insert(self, val):
            maillon = biMaillon(val)
            temp = self.start
            if self.start == None:
                self.start = maillon
                maillon.next = self.start
                maillon.past = self.start
            elif self.start.data > val:
                while temp.next != self.start:
                    temp = temp.next
                maillon.next = self.start
                maillon.past = temp
                self.start.past = maillon
                temp.next = maillon
                self.start = maillon
            else:
                while temp.next != self.start and temp.next.data < val:
                    temp = temp.next
                maillon.next = temp.next
                maillon.past = temp
                temp.next.past = maillon
                temp.next = maillon

    # Suppression d'un élément dans la liste circulaire

        def suppression(self, val):
            temp = self.start
            if temp.data == val:
                while temp.next != self.start:
                    temp = temp.next
                temp.next = self.start.next
                self.start.next.past = temp
                self.start = self.start.next
                return True
            while temp.next != self.start and temp.next.data != val:
                temp = temp.next
            if temp.next == self.start:
                return False
            temp.next = temp.next.next
            temp.next.past = temp
            return True
        
class Tpile():
    def __init__(self):
        self.pile = []
        self.isommet = -1

    def est_vide(self):
        return self.isommet == -1
    
    def est_pleine(self):
        return self.isommet == len(self.pile)-1
    
    def empiler(self,val):
        self.isommet = self.isommet + 1
        self.pile.append(val)
        return True

    def depiler(self):
        self.isommet -= 1
        del self.pile[-1]
        return True
    
    def sommet(self):
        return self.pile[self.isommet]

class LPile():

    def __init__(self):
        self.sommet = None
    
    def empiller(self,val):
        maillon = Maillon(val)
        maillon.next = self.sommet
        self.sommet = maillon
    
    def depiller(self):
        self.sommet = self.sommet.next
    
    def est_vide(self):
        return self.sommet == None
    
    def est_pleine(self):
        return False
    
    def sommet(self):
        return self.sommet.val
    
    def verticale(self,nb):
        if nb < 10:
            print(nb)
        else:
            while(nb > 0):
                self.empiller(nb%10)
                nb = nb//10
            while not self.est_vide():
                print(self.sommet())
                self.depiller()
                
    def inverse_pile(self):
        pile = LPile()
        while not self.est_vide():
            pile.empiller(self.sommet())
            self.depiller()
        return pile
    
class Tfile:

    def __init__(self):
        self.tete = None
        self.qeue = None

    def sortie(self):
        if self.tete.next == None:
            del self.tete
            self = Tfile()
        else:
            suivant = self.tete.next
            del self.tete
            self.tete = suivant

    def entree(self,val):
        maillon = Maillon(val)
        if self.tete == None:
            self.tete = maillon
            self.qeue = maillon
        else:
            self.qeue.next = maillon
            self.qeue = maillon

    def est_vide(self):
        return self.tete == None
    
    def est_plein(self):
        return False
    
    def lire_deb(self):
            return self.tete.val
    
    def affiche_f(self):
        file2  = self
        while not file2.est_vide():
            print(file2.lire_deb())
            file2.sortie()

    def affiche_f2(self):
        self.entree("Stop")
        while self.lire_deb() != "Stop":
            print(self.lire_deb())
            self.entree(self.lire_deb())
            self.sortie()

    def recherche_rec(self,val):
        if self.est_vide():
            return False
        elif self.lire_deb() == val:
            return True
        else:
            self.sortie()
            return self.recherche_rec(val)
        
    def segmenter(self):
        Paire = Tfile()
        Impaire = Tfile()
        while not self.est_vide():
            if self.lire_deb()%2 == 0:
                Paire.entree(self.lire_deb())
            else:
                Impaire.entree(self.lire_deb())
            self.sortie()
        
        Resultat = Tfile()
        while not Paire.est_vide():
            Resultat.entree(Paire.lire_deb())
            Paire.sortie()
        while not Impaire.est_vide():
            Resultat.entree(Impaire.lire_deb())
            Impaire.sortie()
        return Resultat
    
#Algo avancé S3

class Arbre:

    #Taille de l'arbre = nombre de noeuds
    #Hauteur de l'arbre = nombre de noeuds sur le chemin le plus long entre la racine et une feuille

    def __init__(self):
        self.racine = None

    def est_vide(self):
        return self.racine == None
    
    def est_plein(self):
        return False
    
    def inserer(self,val):
        if self.est_vide():
            self.racine = Noeud(val)
        else:
            temp = self.racine
            while True:
                if temp.val > val:
                    if temp.gauche == None:
                        temp.gauche = Noeud(val)
                        break
                    else:
                        temp = temp.gauche
                else:
                    if temp.droit == None:
                        temp.droit = Noeud(val)
                        break
                    else:
                        temp = temp.droit
    
    def rechercher(self,val):
        if self.est_vide():
            return False
        else:
            temp = self.racine
            while temp != None:
                if temp.val == val:
                    return True
                elif temp.val > val:
                    temp = temp.gauche
                else:
                    temp = temp.droit
            return False

    def parcours_pre(self):
        res = ""
        pile = []
        temp = self.racine
        while True:
            while temp:
                res += str(temp.val) + " "
                pile.append(temp)
                temp = temp.gauche
            if not pile:
                break
            temp = pile[-1]
            pile = pile[:-1]
            temp = temp.droit
        return res

    def parcours_in(self):
        res = ""
        pile = LPile()
        temp = self.racine
        while True:
            while temp != None:
                pile.empiller(temp)
                temp = temp.gauche
            if pile.est_vide():
                break
            temp = pile.sommet()
            pile.depiller()
            res += str(temp.val) + " "
            temp = temp.droit
        return res
    
    def parcours_post(self):
        res = ""
        pile = []
        temp = self.racine
        while True:
            while temp != None:
                pile.empiller(temp)
                temp = temp.gauche
            if pile.est_vide():
                break
            temp = pile.sommet()
            pile.depiler()
            temp = temp.droit
            res += str(temp.val) + " "
        return res
    
    def parcours_largeur(self):
        res = ""
        file = Tfile()
        file.entree(self.racine)

    def hauteur(self):
        if self.est_vide():
            return 0

class Noeud:

    def __init__(self,val):
        self.val = val
        self.gauche = None
        self.droit = None

    def est_feuille(self):
        return self.gauche == None and self.droit == None


pile = Tpile()

pile.empiler(1)

print(pile.sommet())

print(pile.depiler())

pile.empiler(2)

print(pile.sommet())