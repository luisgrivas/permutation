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
              res = res + str(ind) + " -> " + str(self.mapping[ind]) + "\n "
        return res
    
    def eval(self, element):
        return self.mapping[element]
 

def lcm(*args):
    if len(args) == 1:
        return args[0] 
    elif len(args) == 2:
        return int(args[0]*args[1] / math.gcd(args[0],args[1]))
    else:
        return lcm(args[0], lcm(args[1], args[2]))


def equal(perm1, perm2):
    if perm1.mapping == perm2.mapping:
        return True
    else:
        return False


def product(perm1, perm2):
    return Permutation([perm1.mapping[val] for val in perm2.mapping])
    

def rand_permutation(n):
    return Permutation(rand.sample(list(range(n)), n))
    

def identity(n):
    return Permutation(list(range(n)))


def orbit(perm, element):
    ind = 0
    res = [element]
    while element != perm.eval(res[ind]):
        res.append(perm.eval(res[ind]))
        ind +=1
    return set(res)


def all_orbits(perm):
    diff = set(range(perm.n_elements))
    res = []
    while bool(diff):
        tmp = orbit(perm, list(diff)[0])
        res.append(tmp)
        diff = diff.difference(tmp)
    return res


def gen_cycle(perm, element):
    tmp = orbit(perm, element)
    return Permutation([index if index not in tmp else perm.eval(index)
            for index in range(perm.n_elements)])


def cycle_decom(perm):
    tmp = all_orbits(perm)
    return [gen_cycle(perm, list(index)[0]) for index in tmp if len(index) > 1]


def iscycle(perm):
    if len(cycle_decomposition(perm)) > 1:
        return True
    else:
        return False


def order(perm):
    tmp = [len(orbit(perm, val)) for val in range(perm.n_elements)]
    index = 0
    res = tmp[0]
    while index < len(tmp) - 1:
        res = lcm(res, tmp[index + 1])
        index += 1
    return res

def power(perm, n):
    if n == 0:
        return identity(perm.n_elements)
    else:
        return product(power(perm, n - 1), perm)


def cyclic_group(perm):
    n = order(perm)
    return [power(perm, ind) for ind in range(n)]