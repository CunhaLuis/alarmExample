#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:50:39 2018

@author: luis
"""


from flask import Flask

from flask_apscheduler import APScheduler


import requests
import random
import os

class Config(object):
    JOBS = [
        {
            'id': 'post_alarm',
            'func': 'doctorOffice:post_alarm',
            'trigger': 'interval',
            'seconds': int(os.environ['SECONDS']),
        }
    ]

    SCHEDULER_API_ENABLED = True
app = Flask(__name__)
app.config.from_object(Config())





def post_alarm():
    data = {"doctorName": os.environ['NAME'], 'value': random.randint(0, 200)}

    url = os.environ['POSTURL']
    r = requests.post(url, json=data)
    print(r.text)

scheduler = APScheduler()
# it is also possible to enable the API directly
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


@app.route("/")
def start():
    post_alarm()
    return "Hello world!"


if __name__ == '__main__':
    app.run()
