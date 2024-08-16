#%%
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from read_csv import readfile

filename='test.csv'
x,y=readfile(filename)

#Below is Nth model and utilize ODE to fit models. Initial guess didn't work
def f(y,t,a,b):
    return a*(b-y)**1; "a=k1, b=Qe, y=Qt,c=n" 

def norder(t,a,b, y0):
    """
    solution to the ODE y'(t)=f(t,y,a,b) with initial condition y(0)=y0
    """
    norder=odeint(f, y0, t, args=(a,b))
    return norder.ravel()

#a=Qmax, b=k for below models
def second(time,a,b):
    return b*a**2*time/(1+a*b*time)

def first(time,a,b):
    return a*(1-np.exp(-b*time))

def intra(time,a,b):
    return a*time**0.5+b

def r_square(x,y,model,popt):
    residuals=y-model(x,*popt)
    ss_res=np.sum(residuals**2)
    ss_tot=np.sum((y-np.mean(y))**2)
    r2=1-(ss_res/ss_tot)
    return r2

def graph(x,y,xdata,ydata,key, r_2):
    plt.figure()
    plt.title(key)
    plt.plot(x,y,'o', label='data')
    plt.plot(xdata,ydata,'r-', label='fit and r2: %5.3f' % r_2)
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('concentration')

models={'First-order model': first, 'Second-order model': second, 
        'Nth-order model': norder, 'Intra Diffusion model': intra}

for key, model in models.items():
    
    if key=='Nth-order model':
        params=[0.02,50,0.5]
    else:
        params=[0, 0.1]
    
    popt,pcov=curve_fit(model,x,y, p0=params)
    xdata=np.linspace(0,4320,400)
    ydata=model(xdata,*popt)
    r_2=r_square(x,y,model,popt)
    graph(x,y,xdata,ydata,key,r_2)


# %%
