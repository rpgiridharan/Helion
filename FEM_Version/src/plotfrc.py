import readxtor as rx
import plotxtor as px
import numpy as np
import matplotlib.pyplot as plt

Z = rx.RawReadField('FRC','ZZ')
R = rx.RawReadField('FRC','RR')
psi = rx.RawReadField('FRC','psi2d')
px.Figure(Z,R,psi,equal=False,fignumber=1)
plt.xlabel('Z'); plt.ylabel('R')

P = rx.RawReadField('FRC','Pressure')
S = rx.RawReadField('FRC','S')
J = rx.RawReadField('FRC','JacobMesh')
Vprime = np.mean(J[:,:-1],axis=1)
plt.figure(2)
plt.clf()
px.Plot(S,P*Vprime**(5/3),lw=2)
plt.xlabel('$S$'); plt.ylabel('$PV\'^{5/3}$')

ZM = rx.RawReadField('FRC', 'ZMesh')
RM = rx.RawReadField('FRC', 'RMesh')
npsi, ntheta = ZM.shape
PsiM = rx.RawReadField('FRC','PsiMesh')
PsiM = np.reshape(np.repeat(PsiM,ntheta),(npsi,ntheta))
px.Figure(ZM,RM,PsiM,equal=False,fignumber=3)
plt.xlabel('Z'); plt.ylabel('R')