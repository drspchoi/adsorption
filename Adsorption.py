import os
from read_csv import readfile
from adsorption_model import kinetic_models, isotherm_models
from flask import Flask, render_template, request

app=Flask(__name__)
folder='static' 
app.config['upload']=folder

@app.get('/')
def index():
    return render_template('adsorption_plot.html')

@app.route('/upload', methods=['POST'])
def upload():

    if 'file' not in request.files and 'file2' not in request.files:

        return "No file part"
    
    if request.files['file']=='' and request.files['file2']=='':
        return "No file uploaded"
    
    selection=[]
    selection2=[]

    if 'file' in request.files:
        file=request.files['file']
        if file.filename:
            file_path=os.path.join(app.config['upload'], file.filename)
            file.save(file_path)
            print(file.filename)        
            x,y=readfile(file.filename)
            selection=request.form.getlist('Kinetic_model')
            kinetic_models(x,y,selection)

    if 'file2' in request.files:
        file2=request.files['file2']
        if file2.filename !='':
            file2_path=os.path.join(app.config['upload'], file2.filename)
            file2.save(file2_path)             
            x,y=readfile(file2.filename)
            selection2=request.form.getlist('isotherm_model')
            isotherm_models(x,y,selection2)

    return render_template('adsorption_plot.html', kinetic=selection, adsorption=selection2)

if __name__== '__main__':
    app.run(debug=True)
