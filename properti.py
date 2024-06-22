class Titik(object):
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, nilai):
        if (not isinstance(nilai, int)) and (not isinstance(nilai, float)):
            raise TypeError('x must numerik type')
        self.__x = nilai

    @x.deleter
    def x(self):
        del self.__x #delete self.__x from memory

    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, nilai):
        if (not isinstance(nilai, int)) and (not isinstance(nilai, float)):
            raise TypeError('y must numerik type')
        self.__y = nilai

    @y.deleter
    def y(self):
        del self.__y #delete self.__y from memory

#create object from titik class
A = Titik()
B = Titik(10, 20)

#determine __x and __y values in A through x and y properties
A.x = 4
A.y = 5

#get __x and __y values in A through x and y properties 
print('A(%d, %d)' % (A.x, A.y))

#determine __x and __y values in B through x and y properties

print('B(%d, %d)' % (B.x, B.y))