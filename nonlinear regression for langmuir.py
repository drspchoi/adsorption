# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:57:49 2017

@author: CHOI
"""

import numpy as np
from scipy.optimize import curve_fit
import pylab

x=np.array([5.60, 40.43, 101.71, 195.07, 289.57])
y=np.array([188.81, 319.08, 396.57, 409.86,420.86])

def langmuir(concent,a,b):
    n=concent.size
    p=np.zeros(n)
    for i in range (n):
        p[i]=a*b*concent[i]/(1+b*concent[i])
    return p

params=[100, 0]
popt,pcov=curve_fit(langmuir,x,y,p0=params)
xdata=np.linspace(0,300,100)
yfit=langmuir(xdata,popt[0], popt[1])
print(popt[0], popt[1])
pylab.plot(x,y,'.',xdata,yfit)

for equil in yfit:
    print(equil)

ysize=yfit.size
xsize=xdata.size
for i in range(ysize):
    print(yfit[i])
    
for conc in xdata:
    print(conc)

for j in range(xsize):
    print(xdata[j])
    
residuals=y-langmuir(x,popt[0],popt[1])
ss_res=np.sum(residuals**2)
ss_tot=np.sum((y-np.mean(y))**2)
r2=1-(ss_res/ss_tot)
print(r2)
