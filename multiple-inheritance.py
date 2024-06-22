#define first superclass
class Induk1(object):
    def __init__(self, a):
        self.a = a
    def cetakA(self):
        print('a value: ', self.a)

#define second superclass
class Induk2(object):
    def __init__(self, b):
        self.b = b
    def cetakB(self):
        print('b value: ', self.b)
#define subclass
class Anak(Induk1, Induk2):
    def __init__(self, a, b, c):
        Induk1.__init__(self, a)
        Induk2.__init__(self, b)
        self.c = c
    def cetakC(self):
        print('c value: ', self.c)

#create object from subclass
obj = Anak(123, 234, 345)

#call method class Induk1 from obj
obj.cetakA()
#call method class Induk2 from obj
obj.cetakB()
#call method subclass
obj.cetakC()
