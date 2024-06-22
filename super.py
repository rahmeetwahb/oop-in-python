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

# define subclass
class KotakWarna(Kotak):
    def __init__(self, p, l, t, w):
        super().__init__(p, l, t)
        # update new attribute
        self.warna = w

    def cetakData(self):
        super().cetakData()
        print('warna: ', self.warna)

#create KotakWarna object
kotakwarna1 = KotakWarna(3, 3, 3, 'Yellow')

#use object
kotakwarna1.cetakData()
kotakwarna1.cetakHasil()