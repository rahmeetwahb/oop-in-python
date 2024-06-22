class Kotak(object):
    def __init__(self, p=0, l=0, t=0):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    def setData(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    def hitung(self):
        return self.panjang * self.lebar / self.tinggi
    
    def cetakData(self):
        print('panjang: ', self.panjang)
        print('lebar: ', self.lebar)
        print('tinggi: ', self.tinggi)

    def cetakHasil(self):
        print('hasil: ', self.hitung())

#create first object with kontructor no parameter
kotak1 = Kotak()
kotak1.setData(5, 5, 5)
print('first object')
kotak1.cetakData()
kotak1.cetakHasil()

#create second object with konstructor and parameter
kotak2 = Kotak(7, 7, 7)
print('second object')
kotak2.cetakData()
kotak2.cetakHasil()