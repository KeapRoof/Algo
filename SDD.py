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
