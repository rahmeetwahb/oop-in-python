class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    
    def hitung(self):
        return self.panjang * self.lebar / self.tinggi
    
    def cetak(self):
        print('panjang\t: ', self.panjang)
        print('lebar\t: ', self.lebar)
        print('tinggi\t: ', self.tinggi)

    def cetakHasil(self):
        print('volume\t: ', self.hitung())

#create frist object
kotak1 = Kotak(9, 4, 2)

#use frist object
print('onject kotak1')
kotak1.cetak()
kotak1.cetakHasil()

#create second object
kotak2 = Kotak(5, 7, 9)

# use second object
print('object kotak2')
kotak2.cetak()
kotak2.cetakHasil()