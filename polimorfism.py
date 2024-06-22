from abc import ABCMeta, abstractmethod
import math

class Bangun3D(metaclass=ABCMeta):
    #define method class
    @abstractmethod
    def cetakData(self):
        pass
    @abstractmethod
    def hitung(self):
        pass
    @abstractmethod
    def cetakHitung(self):
        pass

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

obj = Kotak(5, 6, 7)
print('Balok')
obj.cetakData()
obj.cetakHitung()

del obj

obj = Kotak(7)
print('Kubus')
obj.cetakData()
obj.cetakHitung()

del obj

obj = Tabung(8, 7)
print('Tabung')
obj.cetakData()
obj.cetakHitung()