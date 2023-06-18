


print(' **********************')
print(' Assignment 9-9 ')
print(' **********************','\n')


class Complex:

    def __init__(self,first,second):

        self.num = first
        self.den = second

    def show(self):
        print(self.num, "+ j", self.den)

    def __add__(self, othercomplex):
        newnum = self.num + othercomplex.num
        newden = self.den + othercomplex.den

        return Complex(newnum, newden)


    def __del__(self, othercomplex):
        newnum = self.num - othercomplex.num
        newden = self.den - othercomplex.den

        return Complex(newnum, newden)



myfraction = complex(3,5)

f1 = Complex(1,4)
f2 = Complex(2,6)

f1.show()
f2.show()

f1.__add__(f2).show()

f1.__del__(f2).show()



