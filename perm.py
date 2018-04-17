import random as rand
import math 

class Permutation:
    """Permutation class"""
    
    def __init__(self, map):
        self.mapping = map
        self.n_elements = len(map)
    
    def inverse(self):
        return Permutation([self.mapping[val] for val in self.mapping])
    
    def __repr__(self):
        res = " "
        for ind in range(self.n_elements):
              res = res + "X_" + str(ind) + " -> " + "X_" + str(self.mapping[ind]) + "\n "
        return res
    
    def eval(self, element):
        return self.mapping[element]
    
def product(perm1, perm2):
    return Permutation([perm1.mapping[val] for val in perm2.mapping])

def iscycle(perm):
    return False
    
def rand_permutation(n):
    return Permutation(rand.sample([i for i in range(n)], n))
    
def identity(n):
    return Permutation([i for i in range(n)])

def orbit(perm, element):
    ind = 0
    res = [element]
    while element != perm.eval(res[ind]):
        res.append(perm.eval(res[ind]))
        ind +=1
    return set(res)

def order(perm):
    return [len(orbit(perm, val)) for val in range(perm.n_elements)]

def power(perm, n):
    if n == 0:
        return identity(perm.n_elements)
    else:
        return product(power(perm, n - 1), perm)