#%%
import numpy as np
from scipy.optimize import curve_fit
from read_csv import readfile
#from adsorption_model import norder, second, first, intra, langmuir, Frue, r_square, graph
from adsorption_model import kinetic_models, isotherm_models
from flask import Flask, render_template

app=Flask(__name__)

filename='test.csv'
x,y=readfile(filename)

kinetic_models(x,y)

filename='test2.csv'
x,y=readfile(filename)

isotherm_models(x,y)

@app.get('/')
def plot():
    return render_template('adsorption_plot.html')

if __name__== '__main__':
    app.run(debug=True)
# %%
