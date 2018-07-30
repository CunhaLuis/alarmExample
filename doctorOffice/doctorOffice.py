#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:50:39 2018

@author: luis
"""


from flask import Flask
from flask import render_template
from flask import request


import requests
import pandas as pd
import json
import random
import sys, os



app = Flask(__name__)

@app.route("/")
#@app.cli.command()
#@click.option('--name')
def start():

    
    print('You wanted {!r} directory'.format(app.config.get('name')))
    
    
    data = {"doctorName": os.environ['NAME'], 'value': random.randint(0, 200)}

    url = "http://127.0.0.1:5000/postData/"
    r = requests.post(url, json=data)
    print(r.text)
    
    return "Hello world!"

if __name__ == '__main__':
    app.run()
    
