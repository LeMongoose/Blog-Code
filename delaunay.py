

#from sympy.utilities.iterables import multiset_permutations
import numpy as np

def sequence(n,d):
    for i in range(n):
        yield int ((i&(2**d))/(2**d));

class Delaunay:
    def __init__(self, P, D=None):
        self.P = P
        if D == None:
            D = len(P[0])

        if D < 2:
            raise Exception

        self.D = D
        
        if len(P[0]) != self.D:
            raise Exception
        
        return

    def __box(self):
        _mn = min(self.P,0)
        _mx = max(self.P,0)
        _bounds = np.zeros(self.D,2)
        _bounds[:,0] = _mn
        _bounds[:,1] = mx
        _box = np.zeros(self.D, self.D**2)
        for _d in range(self.D):
            _box[d,:] = sequence(self.D**2, d)
        return _box

    def __great_triangle(self):
        return

    def __call__(self):
        return

def main():
    D = 3
    d = 2
    print(list(sequence(2**D,d)))

if __name__ == "__main__":
    main()