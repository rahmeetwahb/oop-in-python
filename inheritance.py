#define superclass
class Kotak(object):
    def __init__(self, p, l, t):
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
        print('Hasil: ', self.hitung())

#define subclass
class KotakWarna(Kotak):
    def __init__(self, p, l, t, w):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
        self.warna = w

    def cetakData(self):
        print('panjang: ', self.panjang)
        print('lebar: ', self.lebar)
        print('tinggi: ', self.tinggi)
        print('warna: ', self.warna)

#create object kotakwarna
kotakwarna1 = KotakWarna(5, 5, 5, 'blue')

#use object
kotakwarna1.cetakData()
kotakwarna1.cetakHasil()