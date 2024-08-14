# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:57:49 2017

@author: CHOI
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.array([30,60,90,120,240,360,540,1440,2880,4320])
y=np.array([66.31, 82.66, 91.10, 102.77, 127.80, 152.48, 179.30, 236.17,281.58,291.13])

"""
a=Qmax, b=k
"""

def f(y,t,a,b):
    return a*(b-y)**1; "a=k1, b=Qe, y=Qt,c=n" 

def norder(t,a,b, y0):
    """
    solution to the ODE y'(t)=f(t,y,a,b) with initial condition y(0)=y0
    """
    
    norder=odeint(f, y0, t, args=(a,b))
    return norder.ravel()

params=[0.02,50 ,0.5]
popt,pcov=curve_fit(norder,x,y,p0=params)
xdata=np.linspace(0,4320,400)
yfit=norder(xdata,popt[0], popt[1], popt[2])
plt.plot(x,y,'.',xdata,yfit)
print(popt[0], popt[1])
"""
for equil in yfit:
    print(equil)
"""
ysize=yfit.size
xsize=xdata.size
for i in range(ysize):
    print(yfit[i])
"""    
for conc in xdata:
    print(conc)
"""
"""
for j in range(xsize):
    print(xdata[j])
"""    
residuals=y-norder(x,popt[0],popt[1],popt[2])
ss_res=np.sum(residuals**2)
ss_tot=np.sum((y-np.mean(y))**2)
r2=1-(ss_res/ss_tot)
print(r2)
