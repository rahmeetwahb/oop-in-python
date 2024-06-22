class Kotak(object):
    ObjectCounter = 0

    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

        #every object is created, objectcounter
        Kotak.ObjectCounter += 1

    def hitung(self):
        return self.panjang * self.lebar / self.tinggi
    
    def cetakData(self):
        print('panjang\t: ', self.panjang)
        print('lebar\t: ', self.lebar)
        print('tinggi\t: ', self.tinggi)

    def cetakHasil(self):
        print('volume\t: ', self.hitung())

#create first object
kotak1 = Kotak(1, 2, 3)

#use first object
print('print first object')
kotak1.cetakData()
kotak1.cetakHasil()
print('objectcounter= ', kotak1.ObjectCounter)

#create second object
kotak2 = Kotak(4, 5, 6)
#use second object
print('print second object')
kotak2.cetakData()
kotak2.cetakHasil()
print('objectcounter= ', kotak2.ObjectCounter)

#create third object
kotak3 = Kotak(7, 8, 9)
#use third object
print('print third object')
kotak3.cetakData()
kotak3.cetakHasil()
print('objectcounter= ', kotak3.ObjectCounter)

