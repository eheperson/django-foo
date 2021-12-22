


class C:
    pass

class D:
    __slots__ = ['x', 'y']

class E(D):
    pass

## try those steps : 
# open terminal and invoke python 
# import test as t
# c = t.C()
# d = t.D()
# c.__dict__
# d.__dict__
# d.__slots__
# e = t.E()
# e.__dict__
# e.__slots__
# e.z=4
# e.__dict__