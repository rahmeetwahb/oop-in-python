class tanggal(object):
    def __init__(self, dd=0, mm=0, yyyy=0):
        self.hari = tanggal.hari = dd
        self.bulan = tanggal.bulan = mm
        self.tahun = tanggal.tahun = yyyy

    @classmethod
    def dariString(cls, strTanggal):
        hari, bulan, tahun = map(int, strTanggal.split('-'))
        objektanggal = cls(hari, bulan, tahun)
        return objektanggal
    
    def cetakTanggal(self):
        BULAN = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
        print("%d %s %d" % (self.hari, BULAN[self.bulan-1], self.tahun))

#create object drom date class
#using general method
obj1 = tanggal(17, 8, 1945)

#create object from date class
#using class method
obj2 = tanggal.dariString("24-11-2001")

#print date
print('date on obj1: ', end='')
obj1.cetakTanggal()
print('date on obj2: ', end='')
obj2.cetakTanggal()