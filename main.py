# Authors: José García,
# Date: --
# Description: File for testing protocols to simulate quantum correlations

import Classic_Teleportation as cltp
import Max_Entanglement as mxe
import Weak_Entanglement as wke
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

    pplus = [0,0,0]
    pminus = [0,0,0]
    mplus = [0,0,0]
    mminus = [0,0,0]
    b = [0,0,0]

    for i in range(10000):
        b[0] = cltp.Protocol(vp,y)
        b[1] = mxe.Protocolbit(vp,y)
        b[2] = wke.Protocolbitweak(y,p)
        for i in range(3):
            if b[i] == 1:
                pplus[i] += 1
            else:
                pminus[i] += 1
        b[0] = cltp.Protocol(vm,y)
        for i in range(3):
            if b[i] == 1:
                mplus[i] += 1
            else:
                mminus[i] += 1

    claspp = [pplus[0]/(pplus[0] + pminus[0]),pplus[1]/(pplus[1] + pminus[1]),pplus[2]/(pplus[2] + pminus[2])]
    claspm = [pminus[0]/(pplus[0] + pminus[0]),pminus[1]/(pplus[1] + pminus[1]),pminus[2]/(pplus[2] + pminus[2])]
    clasmp = [mplus[0]/(mplus[0] + mminus[0]),mplus[1]/(mplus[1] + mminus[1]),mplus[2]/(mplus[2] + mminus[2])]
    clasmm = [mminus[0]/(mplus[0] + mminus[0]),mminus[1]/(mplus[1] + mminus[1]),mminus[2]/(mplus[2] + mminus[2])]

    Data.append([p,claspp[0],claspp[1],claspp[2],quantpp.real,claspm[0],claspm[1],claspm[2],quantpm.real,clasmp[0],clasmp[1],clasmp[2],
                 quantmp.real,clasmm[0],clasmm[1],clasmm[2],quantmm.real])

outfile = open('data','w')

for i in range(len(Data)):
    outfile.write('%.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f  %.5f' %(Data[i][0], 
                Data[i][1],Data[i][2], Data[i][3],Data[i][4], Data[i][5],Data[i][6], Data[i][7],Data[i][8], Data[i][9],Data[i][10],
                Data[i][11],Data[i][12],Data[i][13],Data[i][14], Data[i][15],Data[i][16]) + '\n')
    
outfile.close() 