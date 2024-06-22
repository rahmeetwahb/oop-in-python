class Kotak(object):
    def __init__(self, p, l, t):
            self.panjang = p
            self.lebar = l
            self.tinggi = t
    def hitung(self):
          return self.panjang * self.lebar / self.tinggi
    
kotak1 = Kotak(1, 2, 3)

print('object kotak1')
print('panjang\t: ', kotak1.panjang)
print('lebar\t: ', kotak1.lebar)
print('tinggi\t: ', kotak1.tinggi)
print('volume\t: ', kotak1.hitung())

kotak2 = Kotak(7, 6, 4)

print('object kotak2')
print('panjang\t: ', kotak2.panjang)
print('lebar\t: ', kotak2.lebar)
print('tinggi\t: ', kotak2.tinggi)
print('volume\t: ', kotak2.hitung())

