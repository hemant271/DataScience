# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 06:58:11 2023

@author: HPatidar
"""
import json
import pickle

__locations = None
__data_columns = None
__model = None

def get_estimated_price():
    

def get_location_names():
    # with open("./artifacts/columns.json","r") as f:
    #     __data_columns = json.load(f)['data_columns']
    #     __locations = __data_columns[3:]
        
    return __locations

def load_saved_artifacts():
    print("loding saved artifacts... start")
    global __data_columns
    global __locations
    
    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        
    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
        
    print("loading saved artifacts...done")
        
        
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())