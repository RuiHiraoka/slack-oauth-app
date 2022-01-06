# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:33:44 2021

@author: ruihi
"""

import flask,requests
from main import app
import os

@app.route('/')
def show_entries():
    print('POST',flask.request.form)
    print('GET',flask.request.args)
    code  = flask.request.args['code']
    print(code)
    data ={'code':code,
           'client_id': os.environ['CLIENT_ID'],
           'client_secret': os.environ['CLIENT_SECRET'],
           'redirect_uri': os.environ['REDIRECT_URL']}

    res = requests.post('https://slack.com/api/oauth.v2.access', data=data)
    
    print('response',res)
    print(res.text)
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'redirected_Hello!!'