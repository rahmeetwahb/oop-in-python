import math

#define abstrac class
class Bangun3D(object):
    #define abstrac method
    def cetakData(self):
        raise NotImplementedError
    def hitung(self):
        raise NotImplementedError
    def cetakHitung(self):
        raise NotImplementedError
    
#define concrid class
class Kotak(Bangun3D):
    def __init__(self, p, l=None, t=None):
        if l == None and t == None:
            self.panjang = self.lebar = self.tinggi = p
        else:
            self.panjang = p
            self.lebar = l
            self.tinggi = t

    #implement methd cetakData()
    def cetakData(self):
        print('panjang: ', self.panjang)
        print('lebar: ', self.lebar)
        print('tinggi: ', self.tinggi)

    #implement method hitung()
    def hitung(self):
        return self.panjang * self.lebar / self.tinggi
    
    #implement method cetakHitung()
    def cetakHitung(self):
        print('Hasil: ', self.hitung())

class Tabung(Bangun3D):
    def __init__(self, r, t):
        self.jarijari = r
        self.tinggi = t

    #implement method cetakData()
    def cetakData(self):
        print('Jarijari: ', self.jarijari)
        print('Tinggi: ', self.tinggi)

    #implement method hitung
    def hitung(self):
        return math.pi * pow(self.jarijari, 2) * self.tinggi
    
    #implement method cetakHitung()
    def cetakHitung(self):
        print('Hasil: ', self.hitung())


obj1 = Kotak(3, 4, 5)
print('balok')
obj1.cetakData()
obj1.cetakHitung()

obj2 = Kotak(5)
print('Kubus')
obj2.cetakData()
obj2.cetakHitung()

obj3 = Tabung(8, 6)
print('tabung')
obj3.cetakData()
obj3.cetakHitung()