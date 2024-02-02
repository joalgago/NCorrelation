# Authors: José García, Yuvraj Thapa, 
# Date: --
# Description: Implementation of the "Classical teleportation" protocol

def Alice_state():
    v = []
    return v

def Classical_c1(v,lambda1,lambda2):
    c1 = 0
    return c1

def Classical_c2(v,lambda1,lambda2,c):
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
    return p
