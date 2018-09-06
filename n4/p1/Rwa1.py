import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

data=pd.read_excel('Tutorial_4.xlsx')
dataset=data.values

Y=dataset[:5697,0]
Y=Y.reshape(Y.shape[0],1)
GR=dataset[:5697,2]
GR=GR.reshape(GR.shape[0],1)
RHOb=dataset[:5697,-1]
RHOb=RHOb.reshape(RHOb.shape[0],1)
Ro=dataset[:5697,7]
Ro=Ro.reshape(Ro.shape[0],1)
NPOR=dataset[:5697,-2]
NPOR=NPOR.reshape(NPOR.shape[0],1)

###################TEMP LOG GENERATION##########
T=70+0.01*Y
T=(T-32)*5/9

###################PRESSURE LOG GENERATION##########
P=0.45*Y
P=P*0.006895

#################ENVIRONMENT VARIABLES##########
RHOsh=2.52 #Smectite
RHOmatrix=2.71 #Carbonate matrix
RHOwater=1+(1/1000000*(-80*T-3.3*T*T+0.00175*T*T*T+489*P-2*T*P+0.016*T*T*P-1.3/100000*T*T*T*P-0.333*P*P-0.002*T*P*P)) #pure water

###################GR PLOT######################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(GR[:],Y[:])
plt.axis([0, 200, 22750, 19900])
plt.xlabel("GR")
plt.show()

###################ESTIMATING Vsh################
GRclean=np.amin(GR,axis=0)
GRshale=np.amax(GR,axis=0)
Vsh=(GR-GRclean)/(GRshale-GRclean)

###################NPOR PLOT#####################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(NPOR[:],Y[:])
plt.axis([3, 1, 22750, 19900])
plt.xlabel("NPOR")
plt.show()

##################POROSITY#######################
PHI=(((Vsh*RHOsh)+(1-Vsh)*RHOmatrix)-RHOb)/(((Vsh*RHOsh)+(1-Vsh)*RHOmatrix)-1)


####################Initial PHI PLOT#####################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(PHI[:],Y[:])
plt.axis([1, 2, 22750, 19900])
plt.xlabel("Initial PHI")
plt.show()
####################Initial Rwa PLOT####################
Rwa=np.multiply(Ro,np.power(PHI,2))

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(Rwa[:],Y[:])
plt.axis([0, 10, 22750, 19900])
plt.xlabel("Rwa Initial")
plt.show()

###################CALCULATING SALINITY#########
PHIprev=PHI
for i in range(10):
    Rwa=np.multiply(Ro,np.power(PHIprev,2))
    S=np.power(10,(1/0.995*(np.log10(3647.5)-np.log10(Rwa*(T[4881]/81.77+6.77/81.77)-0.0123))))
    S=S/1000000
    RHOfluid=RHOwater+S*(0.668+0.44*S+1/1000000*(300*P-2400*P*S+T*(80+3*T-3300*S-13*P+47*P*S)))
    PHI=(((Vsh*RHOsh)+(1-Vsh)*RHOmatrix)-RHOb)/(((Vsh*RHOsh)+(1-Vsh)*RHOmatrix)-RHOfluid)
    PHIprev=PHI


####################Salinity PLOT####################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(S[:],Y[:])
plt.axis([0, 0.003, 22750, 19900])
plt.xlabel("Salinity")
plt.show()


####################Revised PHI PLOT#####################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(PHI[:],Y[:])
plt.axis([1, 2, 22750, 19900])
plt.xlabel("Revised PHI")
plt.show()

####################Revised Rwa PLOT####################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(Rwa[:],Y[:])
plt.axis([0, 10, 22750, 19900])
plt.xlabel("Rwa Revised")
plt.show()
