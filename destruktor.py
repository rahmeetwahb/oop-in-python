class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    def __del__(self):
        print('destructor is called')
    
    def hitung(self):
        return self.panjang * self.lebar / self.tinggi
    
    def cetak(self):
        print('panjang\t: ', self.panjang)
        print('lebar\t: ', self.lebar)
        print('tinggi\t: ', self.tinggi)

    def cetakHasil(self):
        print('volume\t: ', self.hitung())

#create object
kotak1 = Kotak(6, 3, 9)

#use object
kotak1.cetak()
kotak1.cetakHasil()

#delete object manually
del kotak1