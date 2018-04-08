# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# things to do
# 1. file modularization(chop all instances into separate files)
# 2. better understanding of MessagingAPI
# 3. better performance(currently way too slow)

import os

import json
# importing AskKonkuk() from mycode.py
from parser import pos_tagger

from flask import Flask, request, abort, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    # output = pos_tagger('아니시발 이걸영화라고 쳐 만들었냐 그냥나가뒤지시는걸 추천합니다욬ㅋㅋㅋ')
    
    # for s in output:
        # return s
    # print (output)
    
    return 'ok'
    
@app.route("/test", methods=['POST'])
def microsoft():

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    print ("\n\n" + body + "\n\n")
    return 'HELLO'
    
    
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    # signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # print ("\n\n" + body + "\n\n")
    output = pos_tagger(body)
    print(pos_tagger(body))
    
    return json.dumps(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)