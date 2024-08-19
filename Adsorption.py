#%%
import numpy as np
from scipy.optimize import curve_fit
from read_csv import readfile
from adsorption_model import norder, second, first, intra, langmuir, Frue, r_square, graph

filename='test.csv'
x,y=readfile(filename)

kinetic_models={'First-order model': first, 'Second-order model': second, 
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

filename='test2.csv'
x,y=readfile(filename)

isotherm_models={'Langmuir': langmuir, 'Frue': Frue}

for key, model in isotherm_models.items():

    params=[100,0.1]
    popt,pcov=curve_fit(model,x,y, p0=params)
    xdata=np.linspace(0,300,100)
    ydata=model(xdata,*popt)
    r_2=r_square(x,y,model,popt)
    graph(x,y,xdata,ydata,key,r_2)    

# %%
