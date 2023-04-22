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


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    app.run()
    