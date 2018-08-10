#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 11:26:44 2018

@author: luis
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import pandas as pd
import json

high = 180
medium = 120
low = 80

alarms = pd.DataFrame([[pd.Timestamp.utcnow(), "Carolyn", "low"],[pd.Timestamp.utcnow(), "Luis", "medium"]],columns=['time', 'doctor_office', 'level'])

app = Flask(__name__)

@app.route("/")
def start():
    
    
    return render_template('index.html', alarms=alarms)

@app.route("/postData", methods=['post'])
def postData():
    global alarms
    data = request.get_json()
    value = data['value']
    doctor = data['doctorName']
    
    
    
    if value >= low:
        alarms = alarms.append(pd.DataFrame([[pd.Timestamp.utcnow(), doctor, "high" if value>=high else "medium" if value >=medium else "low"]], columns=['time', 'doctor_office', 'level']) )
    else:
        print("nothing!")
    
    return "Value is = {}".format(value) 


@app.route("/updateData/", methods=['get'])
def getData():
     
    jsonObj = alarms.to_json(orient="records")
    #jsonObj = alarms.to_json()
    
    #return alarms
    #return json.dumps(jsonObj)
    return jsonify(jsonObj)
