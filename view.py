# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:25:27 2021

@author: Shayantani Kar
"""


import pickle
from flask import Flask, request, render_template


model = pickle.load(open('final_model.sav', 'rb')) 


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hackanova.html')


@app.route('/predict', methods =['POST'])
def predict():
    

    var = request.form.values()

    prediction = model.predict([var])
    prob = model.predict_proba([var])

    
    return render_template('hackanova.html',result = "{}".format(prediction[0]))

if __name__ == '__main__':
#Run the application
    app.run()
