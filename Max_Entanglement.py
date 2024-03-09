# Authors: José García,
# Date: --
# Description: Implementation of the 1 bit protocol for maximally entangled qubits

from random import randrange

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

def Bit(v,lambda0,lambda1):
    c = 0
    sum1 = 0
    sum2 = 0
    for i in range(3):
        sum1 += v[i]*lambda0[i]
        sum2 += v[i]*lambda1[i]
    if abs(sum2)>abs(sum1):
        c = 1
    return c

def Lambda(c,lambda0,lambda1):
    lam = []
    if c == 0:
        lam = lambda0
    else:
        lam = lambda1
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

def Protocolbit(v,y):
    lambda0 = Normalized_state()
    lambda1 = Normalized_state()
    c = Bit(v,lambda0,lambda1)
    vec = Lambda(c,lambda0,lambda1)
    b = Bob_output(y,vec)
    return b