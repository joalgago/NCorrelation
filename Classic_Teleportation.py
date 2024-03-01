# Authors: José García, Yuvraj Thapa, Yasemin Poyraz Koçak
# Date: --
# Description: Implementation of the "Classical teleportation" protocol for a two qubit system

from random import randrange

def random_quantum_state():
    first_entry = randrange(-100,101)
    second_entry = randrange(-100,101)
    third_entry = randrange(-100,101)
    length_square = first_entry**2+second_entry**2
    while length_square == 0:
        first_entry = randrange(-100,101)
        second_entry = randrange(-100,101)
        third_entry = randrange(-100,101)
        length_square = first_entry**2+second_entry**2+third_entry**2
    first_entry = first_entry / length_square**0.5
    second_entry = second_entry / length_square**0.5
    third_entry = third_entry / length_square**0.5
    return [first_entry, second_entry, third_entry]

def initialize_vector(quantum_state):
    length_square = 0
    for i in range(len(quantum_state)):
        length_square += quantum_state[i]**2
    #print("summation of entry squares is",length_square)
    # there might be precision problem
    # the length may be very close to 1 but not exactly 1
    # so we use the following trick
    if (length_square - 1)**2 < 0.00000001:
        return True
    return False

def Random_vector():
    v = []
    while(initialize_vector(v) != True):
        v = random_quantum_state()
    #print(v)
    return v

def Classical_c1(v,lambda1,lambda2):
    c1 = 0
    sum1 = 0
    sum2 = 0
    for i in range(3):
      sum1 += v[i]*lambda1[i]
      sum2 += v[i]*lambda2[i]
    if abs(sum2)>abs(sum1):
      c1 = 1
    return c1

def Classical_c2(v,lambda1,lambda2,c):
    c2 = 1
    sum = 0
    for i in range(3):
      if c == 0:
        sum += v[i]*lambda1[i]
      else:
        sum += v[i]*lambda2[i]
    if sum < 0:
      c2 = 0
    return c2

def Bob_lambda(c1,c2,lambda0,lambda1):
    lam = []
    if c1 == 0:
      if c2 == 0:
        for j in range(0,3):
          lambda0[j] = -1*lambda0[j]
          lam.append(lambda0[j])
      elif c2 == 1:
        for j in range(0,3):
          lam.append(lambda0[j])
    elif c1 == 1:
      if c2 == 0:
        for j in range(0,3):
          lambda1[j] = -1*lambda1[j]
          lam.append(lambda1[j])
      elif c2 == 1:
        for j in range(0,3):
          lam.append(lambda1[j])
    return lam
    
def Bob_output(y,lam):
    b = 0
    y_dot_lambda = 0
    for i in range(0,3):
      y_dot_lambda = y_dot_lambda + y[i]*lam[i]
    if y_dot_lambda == 0:
      b = b + 0
    elif y_dot_lambda > 0:
      b = b + 1
    elif y_dot_lambda < 0:
      b = b - 1
    return b
    
def Bob_probabilities(b,y,v):
    p = 0
    if b > 0:
        for i in range(0,3):
            p += y[i]*v[i]
        p = (1 + p)/2
    elif b < 0:
        for i in range(0,3):
            p += y[i]*v[i]
        p = (1 - p)/2
    return p

def Protocol(v,y):
  vec0 = Random_vector()
  vec1 = Random_vector()
  c1 = Classical_c1(v,vec0,vec1)
  c2 = Classical_c2(v,vec0,vec1,c1)
  lam = Bob_lambda(c1,c2,vec0,vec1)
  b = Bob_output(y,lam)
  return b