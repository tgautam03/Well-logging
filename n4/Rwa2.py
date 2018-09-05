import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel('Tutorial_4.xlsx')
dataset=data.values
Y=dataset[5874:9980,0]
Y=Y.reshape(Y.shape[0],1)
GR=dataset[5874:9980,2]
GR=GR.reshape(GR.shape[0],1)
RHOb=dataset[5874:9980,-1]
RHOb=RHOb.reshape(RHOb.shape[0],1)
Ro=dataset[5874:9980,7]
Ro=Ro.reshape(Ro.shape[0],1)
NPOR=dataset[5874:9980,-2]
NPOR=NPOR.reshape(NPOR.shape[0],1)
#################ENVIRONMENT VARIABLES##########
RHOsh=2.52 #Smectite
RHOmatrix=2.71 #Carbonate matrix
RHOfluid=1 #pure water
###################GR PLOT######################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(GR[:],Y[:])
plt.axis([0, 200, 24890, 22837])
plt.show()
###################NPOR PLOT#####################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(NPOR[:],Y[:])
plt.axis([3, 1, 24890, 22837])
plt.show()

###################ESTIMATING Vsh################
GRclean=np.amin(GR,axis=0)
GRshale=np.amax(GR,axis=0)
Vsh=(GR-GRclean)/(GRshale-GRclean)
##################POROSITY#######################
PHI=(((Vsh*RHOsh)+(1-Vsh)*RHOmatrix)-RHOb)/(((Vsh*RHOsh)+(1-Vsh)*RHOmatrix)-1)
####################PHI PLOT#####################
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(PHI[:],Y[:])
plt.axis([1, 2, 24890, 22837])
plt.show()
####################Rwa PLOT####################
Rwa=np.multiply(Ro,np.power(PHI,2))
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(Rwa[:],Y[:])
plt.axis([-10, 10, 24890, 22837])
plt.show()
