#%%
import csv
import numpy as np

filename='test.csv'
def readfile(filename):
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        csvFile=csv.reader(file)
    
        xData=[]
        yData=[]
    
        for lines in csvFile:
            if lines[0]=='x':
                continue
            else:
                xData.append(float(lines[0]))
            if lines[1]=='y':
                continue
            else:
                yData.append(float(lines[1]))
        
    return np.array(xData),np.array(yData)

# %%
