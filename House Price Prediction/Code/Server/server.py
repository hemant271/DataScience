# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 06:27:16 2023

@author: HPatidar
"""

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')

def hello():
    return "Hi"

@app.route('/get_location_names')

def get_location_names():
    response = jsonify({
            'locations' : util.get_location_names()
        })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods = ['POST'])

def predict_home_price():
    
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    try:
        response = jsonify({
                'estimated_price' : util.get_estimated_price(location, total_sqft, bhk, bath)
                })
    except Exception as err:
        print(err)
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run()
    