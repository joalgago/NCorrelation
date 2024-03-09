# Authors: José García,
# Date: --
# Description: Implementation of the 1 bit protocol for weakly entangled qubits

from random import randrange
from math import ceil

def Random_state():
    vec = []
    for i in range(3):
        a = randrange(-200,201)
        vec.append(a)
    return vec

def Normalized_state():
    sum = 0
    state = Random_state()
    for i in range(3):
        sum += state[i]**2
    for j in range(3):
        state[j] /= sum**0.5
    return state

def Lambda1():
    vec0 = Normalized_state()
    vec1 = Normalized_state()
    lam = []
    if abs(vec0[2]) < abs(vec1[2]):
        lam = vec1
    else:
        lam = vec0
    if lam[2] < 0:
        for i in range(3):
            lam[i] *= -1
    return lam

def Theta(lam):
    val = 0
    if lam[2] < 0:
        val = 0
    else:
        val = lam[2]
    return val

def Alice_bit(p,lam):
    c = 1
    dist = 1-4*(2*p-1)*Theta(lam)
    prob = ceil(dist*100)
    i = randrange(0,100)
    if i < prob:
        c = 0
    return c

def Bob(c,vec0,vec1):
    lam = []
    if c == 0:
        lam = vec0
    else:
        lam = vec1
    return lam

def Bob_output(y,lam):
    b = 0
    sum = 0
    for i in range(3):
        sum += y[i]*lam[i]
    if sum > 0:
        b = 1
    elif sum < 0:
        b = -1
    return b

def Protocolbitweak(y,p):
    lambda0 = Normalized_state()
    lambda1 = Lambda1()
    c = Alice_bit(p,lambda0)
    vec = Bob(c,lambda0,lambda1)
    b = Bob_output(y,vec)
    return b