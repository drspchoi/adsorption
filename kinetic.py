# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:57:49 2017

@author: CHOI
"""

import numpy as np
from scipy.optimize import curve_fit
import pylab

x=np.array([30,60,90,120,240,360,540,1440,2880,4320])
y=np.array([66.31, 82.66, 91.09, 102.77, 127.80, 152.48, 179.30, 236.17,281.58,296.13])

"""
a=Qmax, b=k
"""

def norder(time,a,b,c): 
    n=time.size
    p=np.zeros(n)
    for i in range (n):
        p[i]=a*(1-(1/(1+b*(c-1)*(a**(c-1))*time[i]))**(1/(c-1)))
    return p
def second(time,a,b):
    n=time.size
    p=np.zeros(n)
    for i in range (n):
        p[i]=b*a**2*time[i]/(1+a*b*time[i])
    return p
def first(time,a,b):
    n=time.size
    p=np.zeros(n)
    for i in range (n):
        p[i]=a*(1-np.exp(-b*time[i]))
    return p
def intra(time,a,b):
    n=time.size
    p=np.zeros(n)
    for i in range (n):
        p[i]=a*time[i]**0.5+b
    return p

params=[400, 0.1, 2]
popt,pcov=curve_fit(norder,x,y,p0=params)
xdata=np.linspace(0,4320,400)
yfit=norder(xdata,popt[0], popt[1], popt[2])
pylab.plot(x,y,'.',xdata,yfit)
print(popt[0], popt[1], popt[2])
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
