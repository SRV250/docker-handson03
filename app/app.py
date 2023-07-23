import os, flask, datetime, redis, pytz
from flask import Flask
from flask import render_template
from redis import StrictRedis
from datetime import datetime
from pytz import timezone

PORT = int(os.environ['PORT'])
app = flask.Flask('app server')
HOST = os.environ['HOST']
redis = StrictRedis(host=HOST,port=6379)


@app.route('/')
def index():
    utc_now = datetime.now(timezone('UTC'))
    jst_now = utc_now.astimezone(timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")
    redis.lpush('times',jst_now)
    return render_template('index.html', title='動作確認',times=redis.lrange('times', 0, -1))
    
app.run(debug=True, host='0.0.0.0',port=PORT)