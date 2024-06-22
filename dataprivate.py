class Titik(object):
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    #setter
    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    #getter
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
#create object from titik class
A = Titik()

#determine the values of __x and __y in A
A.setx(6)
A.sety(7)

#get values __x and __y in A
print('A(%d, %d)' % (A.getx(), A.gety()))