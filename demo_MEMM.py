#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Shiyu Huang 
@contact: huangsy13@gmail.com
@file: demo_MEMM.py
"""
from model_MEMM import MODEL_MEMM
from dataflow import MEMM_save_dir, model_path
import pickle

# sentenses = ['重阳节需要登高山', '桃李争春', '暖春天地宽']
# sentenses = ['有志者事竟成，破釜沉舟，百二秦关终属楚']
# sentenses=['一二三四五六七']
sentenses = ['青山不墨千秋画', '两岸凉生菰叶雨', '无边落木萧萧下', '两只黄鹂鸣翠柳',
             '深秋帘幕千家雨', '月透柳帘窥案卷']

def MEMM(sentenses):
    with open(model_path + 'unigram.pkl', 'rb') as f:
        unigram = pickle.load(f)
    with open(model_path + 'memm.pkl', 'rb') as f:
        MEMM_pro = pickle.load(f)
    keep_size = 10

    model = MODEL_MEMM(unigram, MEMM_pro, keep_size=keep_size)

    for sentense in sentenses:
        results = model.test(sentense)
        # print(sentense, results[0][0])
    return results[0][0]
if __name__ == '__main__':
    result_MEMM=MEMM(sentenses)
    print(result_MEMM)