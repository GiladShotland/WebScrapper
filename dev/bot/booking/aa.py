from dev.bot.booking.bb import *


class B(A):
    def __init__(self,j,b,c,d):
        self.a= j
        self.b = b
        self.c = c
        self.d = d
        super(B,self).__init__(j)

if __name__ == '__main__':
    b = B(1,2,3,4)