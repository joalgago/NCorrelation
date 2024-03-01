# Authors: José García,
# Date: --
# Description: File for testing protocols to simulate quantum correlations

import Classic_Teleportation as cltp
from math import sqrt

Data = []
x = cltp.Random_vector()
y = cltp.Random_vector()
prob = []
pin = 1/2
for i in range(11):
    prob.append(round(pin,2))
    pin += 0.05

for p in prob:
    a = sqrt(p-p**2)
    pplus = 1+x[2]*(2*p-1)
    pminus = 1-x[2]*(2*p-1)
    vp = [(2*a*x[0])/pplus,(-2*a*x[1])/pplus,(2*p-1+x[2])/pplus]
    vm =  [(2*a*x[0])/pminus,(-2*a*x[1])/pminus,(-2*p+1+x[2])/pminus]

    mvp = [[1+vp[2],vp[1]-complex(0,vp[0])],[vp[1]+complex(0,vp[0]),1-vp[2]]] 
    mvm = [[1+vm[2],vm[1]-complex(0,vm[0])],[vm[1]+complex(0,vm[0]),1-vm[2]]]
    yplus = [[1+y[2],y[1]-complex(0,y[0])],[y[1]+complex(0,y[0]),1-y[2]]]
    yminus = [[1-y[2],-y[1]+complex(0,y[0])],[-y[1]-complex(0,y[0]),1+y[2]]]

    quantpp = (mvp[0][0]*yplus[0][0]+mvp[1][0]*yplus[0][1]+mvp[1][1]*yplus[1][1]+mvp[0][1]*yplus[1][0])/4
    quantpm = (mvp[0][0]*yminus[0][0]+mvp[1][0]*yminus[0][1]+mvp[1][1]*yminus[1][1]+mvp[0][1]*yminus[1][0])/4
    quantmp = (mvm[0][0]*yplus[0][0]+mvm[1][0]*yplus[0][1]+mvm[1][1]*yplus[1][1]+mvm[0][1]*yplus[1][0])/4
    quantmm = (mvm[0][0]*yminus[0][0]+mvm[1][0]*yminus[0][1]+mvm[1][1]*yminus[1][1]+mvm[0][1]*yminus[1][0])/4

    pplus = 0
    pminus = 0
    mplus = 0
    mminus = 0

    for i in range(10000):
        b = cltp.Protocol(vp,y)
        if b == 1:
            pplus += 1
        else:
            pminus += 1
        b = cltp.Protocol(vm,y)
        if b == 1:
            mplus += 1
        else:
            mminus += 1

    claspp = pplus/(pplus + pminus)
    claspm = pminus/(pplus + pminus)
    errorpp = abs(quantpp.real - claspp)/quantpp.real
    errorpm = abs(quantpm.real - claspm)/quantpm.real
    clasmp = mplus/(mplus + mminus)
    clasmm = mminus/(mplus + mminus)
    errormp = abs(quantmp.real - clasmp)/quantmp.real
    errormm = abs(quantmm.real - clasmm)/quantmm.real

    Data.append([p,claspp,quantpp.real,errorpp*100,claspm,quantpm.real,errorpm*100,clasmp,quantmp.real,errormp*100,clasmm,quantmm.real,errormm*100])

outfile = open('data','w')

for i in range(len(Data)):
    outfile.write('%.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f' %(Data[i][0], Data[i][1], 
                                                                                                   Data[i][2], Data[i][3],
                                                                                                   Data[i][4], Data[i][5],
                                                                                                   Data[i][6], Data[i][7],
                                                                                                   Data[i][8], Data[i][9],
                                                                                                   Data[i][10], Data[i][11], Data[i][12]) + '\n')
    
outfile.close() 