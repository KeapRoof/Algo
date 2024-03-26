from json.encoder import INFINITY


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
    
    
    def parcours_niveaux(self):
        res = ""
        file = Tfile()
        file.entree(self.racine)
        while not file.est_vide():
            temp = file.lire_deb()
            file.sortie()
            res += str(temp.val) + " "
            if temp.gauche != None:
                file.entree(temp.gauche)
            if temp.droit != None:
                file.entree(temp.droit)
        return res
    
    def parcours_pre(abr):
        res = 0
        file = Tpile()
        temp = abr
        while True:
            while temp != None:
                res = res + temp.val
                file.empiller(temp)
                temp = temp.fg
                if(pile.est_vide()):
                    break
                temp = pile.sommet()
                pile.depiler()
                temp.droit
        return res
    

    def inf(abr):
        res = 0
        pile = Pile()
        temp = abr
        while True:
            while(temp != None):
                pile.empiler(temp)
                temp = temp.fg
                if(pile.est_vide()):
                    break
                temp = pile.sommet()
                pile.depiler()
                res = res + temp.val
                temp = temp.fd
        return res
    
    def post(abr):
        res = 0
        pile = Pile()
        temp = abr
        while True:
            while temp != None:
                pile.empiler(temp)
                temp = temp.fg
                if(pile.est_vide()):
                    break
                temp = pile.sommet()
                pile.depiler()
                temp = temp.fd
                res = temp.val + res
        return res

    
    def parcours_niveaux_count(self):
        res = 0
        file = Tfile()
        file.entree(self.racine)
        while not file.est_vide():
            temp = file.lire_deb()
            file.sortie()
            res += 1
            if temp.gauche != None:
                file.entree(temp.gauche)
            if temp.droit != None:
                file.entree(temp.droit)

    def hauteur(self):
        if self.est_vide():
            return 0
        

    def taille_rec(self,noeud):
        #nb de noeuds
        if noeud == None:
            return 0
        else:
            return 1 + self.taille_rec(noeud.gauche) + self.taille_rec(noeud.droit)

    def count_nb_noeuds(self):
        if self.est_vide():
            return 0
        else:
            pile = LPile()
            pile.empiller(self.racine)
            res = 0
            while not pile.est_vide():
                temp = pile.sommet()
                pile.depiler()
                res += 1
                if temp.gauche != None:
                    pile.empiller(temp.gauche)
                if temp.droit != None:
                    pile.empiller(temp.droit)
            return res
        
    def recherche_rec(self, noeud, val):
        if noeud is None:
            return False
        if noeud.val == val:
            return True
        if val != noeud.val:
            return (self.recherche_rec(noeud.gauche, val) or self.recherche_rec(noeud.droit, val))
        
    


class Noeud:

    def __init__(self,val):
        self.val = val
        self.gauche = None
        self.droit = None

    def est_feuille(self):
        return self.gauche == None and self.droit == None
    
a = Arbre()
a.inserer(5)
a.inserer(3)
a.inserer(7)
a.inserer(2)
a.inserer(4)

print(a.parcours_pre())

def mirror(nd):
    if(nd.fg != None or nd.fd != None):
        temp = nd.fg
        nd.fg = nd.fd
        nd.fd = temp
        mirror(nd.fg)
        mirror(nd.fd)

# nb_comp += 1
#def_rec_hauteur(nd):
 #   if nd == None:
  #      return -1
  #  else:
   #     return 1 + max(rec_hauteur(nd.fg),rec_hauteur(nd.fd))

def sup_plus_droit_rec(nd):
        if nd.fd == None & nd.fg == None:
            del nd
        if nd.fd == None:
            return sup_plus_droit_rec(nd.fg)
        else:
            return sup_plus_droit_rec(nd.fd)

def inserer_plus_a_droite(nd,nd_insert):
    if nd.fd == None & nd.fg == None:
        nd.fd =  nd_insert
    if nd.fd == None:
            return sup_plus_droit_rec(nd.fg)
    else:
        return sup_plus_droit_rec(nd.fd)
    
def inserer_plus_a_gauche(nd,nd_insert):
    if nd.fd == None & nd.fg == None:
        nd.fg =  nd_insert
    if nd.fg == None:
            return sup_plus_droit_rec(nd.fd)
    else:
        return sup_plus_droit_rec(nd.fg)

def supprimer(self, noeud, val, parent=None):
    if noeud is None:
        return False
    if noeud.val == val:
        inserer_plus_a_droite(parent,noeud.fd)
        inserer_plus_a_gauche(parent,noeud.fg)
        return True
    if val != noeud.val:
            return (recherche_rec(noeud.gauche, val,noeud) or recherche_rec(noeud.droit, val,noeud))

def trier_tab_abr(tab):
    arbre = Arbre()
    for i in tab:
        planter(arbre,i)
    return arbre.parcours_in()

tab = [5,3,7,2,4]

print(trier_tab_abr(tab))

def planter(abr,val):
    #Ajouter un noeud à l'arbre binaire de recherche
    if abr.est_vide():
        abr.racine = Noeud(val)
    else:
        temp = abr.racine
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


def min_droit(nd):
    #Recherche la valeur minimale du sous-arbre droit
    min = INFINITY
    temp = nd.droit
    min = temp.val
    while temp != None:
        if temp.val < min:
            min = temp.val
        temp = temp.gauche
    return min

def suppresion(abr,val):
    #Supprimer un noeud de l'arbre binaire de recherche
    if abr.est_vide():
        return False
    else:
        temp = abr.racine
        while temp != None:
            if temp.val == val:
                #Cas 1: le noeud est une feuille
                if temp.gauche == None & temp.droit == None:
                    del temp
                    return True
                #Cas 2: le noeud a un seul fils
                elif temp.gauche == None:
                    temp = temp.droit
                    suppresion(temp.gauche,temp.val)
                    return True
                elif temp.droit == None:
                    temp = temp.gauche
                    suppresion(temp.droit,temp.val)
                    return True
                #Cas 3: le noeud a deux fils
                else:
                    temp.val = min_droit(temp)
                    suppresion(temp.droit,temp.val)
                    return True
            elif temp.val > val:
                temp = temp.gauche
            else:
                temp = temp.droit           
        return False
    

def rotation_gauche(nd):
    #Rotation gauche
    temp = nd.droit
    nd.droit = temp.gauche
    temp.gauche = nd
    return temp


def rotation_droite(nd):
    #Rotation droite
    temp = nd.gauche
    nd.gauche = temp.droit
    temp.droit = nd
    return temp

def equilibrage(nd):
    #cas 1: rotation gauche
    if nd.gauche.hauteur() - nd.droit.hauteur() == 2:
        if nd.gauche.gauche.hauteur() > nd.gauche.droit.hauteur():
            rotation_droite(nd)
        else:
            nd.gauche = rotation_gauche(nd.gauche)
            rotation_droite(nd)
    #cas 2: rotation droite
    elif nd.droit.hauteur() - nd.gauche.hauteur() == 2:
        if nd.droit.droit.hauteur() > nd.droit.gauche.hauteur():
            rotation_gauche(nd)
        else:
            nd.droit = rotation_droite(nd.droit)
            rotation_gauche(nd)
    #cas 3: double rotation gauche - droite
    elif nd.gauche.hauteur() - nd.droit.hauteur() == 2:
        nd.gauche = rotation_gauche(nd.gauche)
        rotation_droite(nd)
    #cas 4: double rotation droite - gauche
    elif nd.droit.hauteur() - nd.gauche.hauteur() == 2:
        nd.droit = rotation_droite(nd.droit)
        rotation_gauche(nd)


def rotation_droite(nd):
    #Rotation droite
    temp = nd.gauche.gauche
    temp.droit = nd
    temp.dg = nd.gauche

def rotation_gauche(nd):
    #Rotation gauche
    temp = nd.droit.droit
    temp.gauche = nd
    temp.dd = nd.droit
    
def is_double_gauche(nd):
    return nd.gauche != None and nd.gauche.gauche != None

def is_double_droite(nd):
    return nd.droit != None and nd.droit.droit != None

if(is_double_gauche(nd)):
    rotation_droite(nd)

if(is_double_droite(nd)):
    rotation_gauche(nd)

def equilibrer(nd):
    if(is_double_gauche(nd)):
        rotation_droite(nd)
    if(is_double_droite(nd)):
        rotation_gauche(nd)

def composante_connexe_non_oriente(graphe):
    nb_comp = 0
    parcourue = []
    temp = graphe.entree
    while(True):
        while(temp != None and temp not in parcourue):
            nb_comp += 1
            parcourue.append(temp)
            current = temp.ls
            while(current != None):
                parcourue.append(current.val)
                current = current.next
        temp = temp.next
        parcourue = []
        if(temp == None):
            break
    return nb_comp

def composante_connexe_orienté(graphe):
    nb_comp = 0
    temp = graphe.entre
    while(True):
        while(temp != None and (temp.ariv == None or temp.dep == None)):
            nb_comp += 1
            current = temp.ls
            temp.dep = True # PLUS
            while(current != None):
                marque_ariv(graphe,current.val) # MOINS
                current = current.next
            temp = temp.next
        if(temp == None):
            break
    return nb_comp

def marque_ariv(graphe,nd):
    temp = graphe.entree
    while(temp != None and temp != nd.val):
        temp = temp.next
    temp.ariv = True

def sous_arbre_poids_min(graphe):
    res = Arbre()
    sum = 0
    temp = graphe.entree
    while(temp != None):
        if(temp.ls != None):
            min = temp.ls.val
            current = temp.ls
            dest = current.dest
            while(current != None):
                if(current.val < min):
                    min = current.val
                    dest = current.dest
                current = current.next
            sum += min
            planter(res,dest)
        temp = temp.next
    
    return res,sum,is_all_nd_in_abr(graphe,res)*
    
def kruskal(graphe):
    res = Arbre()
    sum = 0
    all_arretes = []
    used_arretes = []
    temp = graphe.entree
    while(temp != None):
        current = temp.ls
        while(current != None):
            all_arretes.append([temp.val,current.dest,current.val])
            current = current.next
        temp = temp.next
    all_arretes.sort(key=lambda x: x[2])
    for i in all_arretes:
        if(not cycle_or_not(used_arretes)):
            res.planter(res,i)
            sum += i[2]
            used_arretes.append(i)
    return res,sum

def cycle_or_not(liste):
    for i in range(len(liste)):
        temp = liste[i]
        #format liste = [[depart,arrivé,poids],[depart,arrivé,poids]]
        j = 1
        while i + j < len(liste):
            temp2 = liste[i+j]
            if temp2[1] == temp[1]:
                return True
            j += 1
    return False


def is_all_nd_in_abr(graphe,abr):
    temp = graphe.entree
    while(temp != None):
        if(not recherche_rec(abr,temp.val)):
            return False
        temp = temp.next
    return True

def multiple_val_abr_rec(abr):
    #multiplie la valeur de tout les valeurs de l'arbre entre eux
    if abr == None:
        return 1
    else:
        return abr.val * multiple_val_abr_rec(abr.gauche) * multiple_val_abr_rec(abr.droit)
    
def multiple_val_abr_iter(abr):
    #infixe
    pile = LPile()
    temp = abr
    res = 1
    while True:
        while temp != None:
            pile.empiller(temp)
            temp = temp.gauche
        if pile.est_vide():
            break
        temp = pile.sommet()
        pile.depiler()
        res *= temp.val
        temp = temp.droit
    return res