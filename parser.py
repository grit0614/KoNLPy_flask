#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import konlpy
from konlpy.tag import Twitter
tagger_twitter = Twitter()
# output = tagger_twitter.morphs(u'아니시발 이걸영화라고 쳐 만들었냐 그냥나가뒤지시는걸 추천합니다욬ㅋㅋㅋ')

# print (output)


def pos_tagger(raw):
    # payload = raw + ' has been received from /callback'
    payload = tagger_twitter.morphs(raw)
    # output=[]
    # decode to euc-kr
    # payload = [s.encode('utf8') for s in payload]
    # for s in payload:
        # print(s.encode('utf8'))
        # output.append(s.encode('utf8'))
    return payload