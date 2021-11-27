import os, flask, datetime, redis
from flask import Flask
from flask import render_template
from redis import StrictRedis
from datetime import datetime

PORT = int(os.environ['PORT'])
app = flask.Flask('app server')
redis = StrictRedis(host='redis',port=6379)

@app.route('/')
def index():
    redis.lpush('times',datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    return render_template('index.html', title='動作確認',times=redis.lrange('times', 0, -1))
    
app.run(debug=True, host='0.0.0.0',port=PORT)