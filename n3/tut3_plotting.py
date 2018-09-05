import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel('Tutorial_3.xlsx')
dataset=data.values

Y=dataset[:,0]
Y=Y.reshape(Y.shape[0],1)
X=dataset[:,1:]

########GR plot########
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(X[:,0],Y[:])
plt.axis([0, 150, 2364, 2169])
plt.show()

########BS plot########
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(X[:,1],Y[:])
plt.axis([5, 17, 2364, 2169])
plt.show()

########SP plot########
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(X[:,2],Y[:])
plt.axis([-150, 150, 2364, 2169])
plt.show()

########LLD plot########
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(X[:,3],Y[:])
plt.axis([0.1, 100, 2364, 2169])
plt.xscale('log')
plt.show()

########NPHI plot########
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(X[:,4],Y[:])
plt.axis([0.6, 0, 2364, 2169])
plt.show()

########DT plot########
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(X[:,5],Y[:])
plt.axis([140, 40, 2364, 2169])
plt.show()

########RHOZ plot########
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

plt.plot(X[:,6],Y[:])
plt.axis([1.95, 2.95, 2364, 2169])
plt.show()
