

#from sympy.utilities.iterables import multiset_permutations
import numpy as np

def sequence(n,d):
    for i in range(n):
        yield int ((i&(2**d))/(2**d));

def main():
    D = 3
    d = 2
    print(list(sequence(2**D,d)))

if __name__ == "__main__":
    main()