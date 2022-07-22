def nwd(a, b): # funkcja najwiekszy wspolny dzielnik
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


class Wymierna:
    def __init__(self, licz = 0, mian = 1): # constructor
        self.d = None
        self.licz = licz
        self.mian = mian

        self.setNumber(self.licz, self.mian)


    def setNumber(self, _l = 0, _m = 1):
        self.licz = _l
        self.mian = _m
        self.d = nwd(_l, _m) # dzieli przez nwd i skraca do najmniejszych mozliwych liczb

        self.licz = self.licz/self.d
        self.mian = self.mian/self.d

        if self.mian < 0:
            self.mian = self.mian * -1
            self.licz = self.licz * -1


    def set_stoi(self, s):
        # s = string
        if "/" in s:
            s.split("/") # tablica z licznikiem i mianownikiem, utworzona z input string
            self.setNumber(int(s.split("/")[0]), int(s.split("/")[1]))
        else:
            self.setNumber(int(s))


    # def find(self, x): # funkcja szukajaca w zbiorze liczb wymiernych konkretnej liczby wymiernej
    #     if type(self) == list:
    #         for i in self:
    #             if i.l() == x.l() and i.m() == x.m():
    #                 return True
    #             else:
    #                 continue
    #     elif type(self) == Wymierna:
    #         if self.l() == x.l() and self.m() == x.m():
    #             return True
    #         else:
    #             return False
    #     elif type(self) == int or type(self) == float:
    #         return False


    def l(self):
        return int(self.licz)


    def m(self):
        return int(self.mian)



    # operator overload

    def __repr__(self): # overload funkcji repr() i print(), czyli jak ma sie wyswietlac w konsoli object
        if self.licz % self.mian == 0: # skrocenie do liczby nie wymiernej, jesli mozliwe
            repr_overload = str(int(self.l()))
            return repr_overload
        else:
            repr_overload = str(int(self.l())) + "/" + str(int(self.m()))
            return repr_overload


    def __add__(self, obj): # overload dodawania +
        ll = (self.l() * obj.m()) + (self.m() * obj.l()) # licznik obiektu zastepczego
        mm = (self.m() * obj.m()) # mianownik obiektu zastepczego

        return Wymierna(ll, mm)


    def __mul__(self, o): # overload mnozenia *
        ll = self.l() * o.l()
        mm = self.m() * o.m()

        return Wymierna(ll, mm)


    def __lt__(self, o): # overload < (dla sortowania)
        if type(self) == int or type(self) == float: # 1 liczba to int/float
            if self < o.l():
                return True
            else:
                return False
        elif type(o) == int or type(o) == float: # 2 liczba to int/float
            if self.l() < o:
                return True
            else:
                return False
        elif (type(o) == int or type(o) == float) and (type(self) == int or type(self) == float): # obydwie to int/float
            if self < o:
                return True
            else:
                return False
        else: # gdy obydwie to wymierne
            # najpierw trzeba sprowadzic do wspolnego mianownika, potem dopiero porownywac liczniki
            ll1 = self.l() * o.m()

            ll2 = o.l() * self.m()

            if ll1 < ll2:
                return True
            else:
                return False


    def __gt__(self, o):
        if type(self) == int or type(self) == float: # 1 liczba to int/float
            if self > o.l():
                return True
            else:
                return False
        elif type(o) == int or type(o) == float: # 2 liczba to int/float
            if self.l() > o:
                return True
            else:
                return False
        elif (type(o) == int or type(o) == float) and (type(self) == int or type(self) == float): # obydwie to int/float
            if self > o:
                return True
            else:
                return False
        else: # gdy obydwie to wymierne
            # najpierw trzeba sprowadzic do wspolnego mianownika, potem dopiero porownywac liczniki
            ll1 = self.l() * o.m()

            ll2 = o.l() * self.m()

            if ll1 > ll2:
                return True
            else:
                return False


    def __eq__(self, o):
        if type(self) == int or type(self) == float: # 1 liczba to int/float
            if self == o.l():
                return True
            else:
                return False
        elif type(o) == int or type(o) == float: # 2 liczba to int/float
            if self.l() == o:
                return True
            else:
                return False
        elif (type(o) == int or type(o) == float) and (type(self) == int or type(self) == float): # obydwie to int/float
            if self == o:
                return True
            else:
                return False
        else: # gdy obydwie to wymierne
            # najpierw trzeba sprowadzic do wspolnego mianownika, potem dopiero porownywac liczniki
            ll1 = self.l() * o.m()

            ll2 = o.l() * self.m()

            if ll1 == ll2:
                return True
            else:
                return False


    def __hash__(self):
        if type(self) != int:
            hash_value = hash(self.m())
            return hash_value
        elif type(self) != float:
            hash_value = hash(self.m())
            return hash_value
        else:
            hash_value = hash(self)
            return hash_value