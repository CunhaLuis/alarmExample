#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:50:39 2018

@author: luis
"""


from flask import Flask

from apscheduler.schedulers.blocking import BlockingScheduler

import requests
import random
import os

app = Flask(__name__)

sched = BlockingScheduler() # Scheduler object


def post_alarm():
    data = {"doctorName": os.environ['NAME'], 'value': random.randint(0, 200)}

    url = "http://127.0.0.1:5000/postData/"
    r = requests.post(url, json=data)
    print(r.text)


sched.add_job(post_alarm, 'interval',seconds=1)
sched.start()

@app.route("/")
def start():
    post_alarm()
    return "Hello world!"


if __name__ == '__main__':

    app.run()