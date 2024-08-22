import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

"""
First part is for kinetic model equations
"""
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

"""
Second part is for adsorption equilibrium model equations
"""
def langmuir(concent,a,b):
    return a*b*concent/(1+b*concent)

def Frue(concent,k,f):
    return k*concent**f

"""
Third part is for R2 and graph
"""
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
    plt.savefig("static/images/"+key+".png")

def kinetic_models(x,y,selection):
    kinetic_models={'First-order model': first, 'Second-order model': second, 
            'Nth-order model': norder, 'Intra-Diffusion model': intra}

    for key in selection:
    
        if key=='Nth-order model':
            params=[0.02,50,0.5]
        else:
            params=[0, 0.1]
        model=kinetic_models[key]
        popt,pcov=curve_fit(model,x,y, p0=params)
        xdata=np.linspace(0,x.max(),400)
        ydata=model(xdata,*popt)
        r_2=r_square(x,y,model,popt)
        graph(x,y,xdata,ydata,key,r_2)


def isotherm_models(x,y):
    isotherm_models={'Langmuir': langmuir, 'Frue': Frue}

    for key, model in isotherm_models.items():

        params=[100,0.1]
        popt,pcov=curve_fit(model,x,y, p0=params)
        xdata=np.linspace(0,x.max(),100)
        ydata=model(xdata,*popt)
        r_2=r_square(x,y,model,popt)
        graph(x,y,xdata,ydata,key,r_2)    
