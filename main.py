# Authors: José García,
# Date: --
# Description: File for testing protocols to simulate quantum correlations

import Classic_Teleportation as cltp
from math import sqrt

x = cltp.Random_vector()
p = 1/2
a = sqrt(p-p**2)
pplus = 1+x[2]*(2*p-1)
v = [(2*a*x[0])/pplus,(-2*a*x[1])/pplus,(2*p-1+x[2])/pplus]
y = cltp.Random_vector()

mv = [[1+v[2],v[1]-complex(0,v[0])],[v[1]+complex(0,v[0]),1-v[2]]] 
yplus = [[1+y[2],y[1]-complex(0,y[0])],[y[1]+complex(0,y[0]),1-y[2]]]
yminus = [[1-y[2],-y[1]+complex(0,y[0])],[-y[1]-complex(0,y[0]),1+y[2]]]

quantplus = (mv[0][0]*yplus[0][0]+mv[1][0]*yplus[0][1]+mv[1][1]*yplus[1][1]+mv[0][1]*yplus[1][0])/4
quantminus = (mv[0][0]*yminus[0][0]+mv[1][0]*yminus[0][1]+mv[1][1]*yminus[1][1]+mv[0][1]*yminus[1][0])/4
  
vec0 = cltp.Random_vector()
vec1 = cltp.Random_vector()
c1 = cltp.Classical_c1(v,vec0,vec1)
c2 = cltp.Classical_c2(v,vec0,vec1,c1)
lam = cltp.Bob_lambda(c1,c2,vec0,vec1)
b = cltp.Bob_output(y,lam)
prob = cltp.Bob_probabilities(b,y,v)

print("Bob's output:",b)
print("Bob's classical probability",prob)
print("Bob's quantum probability to output +1",quantplus)
print("Bob's quantum probability to output -1",quantminus)