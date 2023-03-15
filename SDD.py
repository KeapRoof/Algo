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
        self.isommet += 1
        self.pile[self.isommet] = val
        return True

    def depiler(self):
        self.isommet -= 1
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