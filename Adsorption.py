
from read_csv import readfile
from adsorption_model import kinetic_models, isotherm_models
from flask import Flask, render_template, request

app=Flask(__name__)

#8/19 Get input from HTML and run scripts (done 8/20). Make a selection list. HTML shows the graph for selected models (done 8/21).
#8/21 Need to make multiple selection possible (done 8/22). Also conditional display needs to be done" 

@app.get('/')
def index():
    return render_template('adsorption_plot.html')

@app.route('/upload', methods=['POST'])
def upload():

    if 'file' not in request.files and 'file2' not in request.files:
        return "No file part"

    print(request.files)
    if 'file' in request.files:
        file=request.files['file']
        if file.filename:
            x,y=readfile(file.filename)
            selection=request.form.getlist('Kinetic_model')
            print(selection)
            kinetic_models(x,y,selection)

    if 'file2' in request.files:
        file2=request.files['file2']
        if file2.filename:
            x,y=readfile(file2.filename)
            selection=request.form.getlist('isotherm_model')
            isotherm_models(x,y,selection)

    return render_template('adsorption_plot.html')

if __name__== '__main__':
    app.run(debug=True)
