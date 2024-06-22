class Kotak(object):
    #variable class
    ObjectCounter = 0

    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
        Kotak.ObjectCounter += 1

    def hitung(self):
        return self.panjang * self.lebar / self.tinggi
    
    def cetakData(self):
        print('panjang\t: ', self.panjang)
        print('lebar\t: ', self.lebar)
        print('tinggi\t: ', self.tinggi)

    def cetakHasil(self):
        print('volume\t: ', self.hitung())

    @staticmethod
    def cetakJudul():
        if Kotak.ObjectCounter > 1:
            print()
        print('Kotak ke-', Kotak.ObjectCounter)

kotak1 = Kotak(8, 4, 2)
Kotak.cetakJudul()
kotak1.cetakData()
kotak1.cetakHasil()

kotak2 = Kotak(9, 6, 3)
Kotak.cetakJudul()
kotak2.cetakData()
kotak2.cetakHasil()

kotak3 = Kotak(6, 5, 4)
Kotak.cetakJudul()
kotak3.cetakData()
kotak3.cetakHasil()