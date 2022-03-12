#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Shiyu Huang 
@contact: huangsy13@gmail.com
@file: demo_HMM.py
"""
from model_HMM import MODEL_HMM
from dataflow import HMM_save_dir, model_path
import pickle

# sentenses = ['重阳节需要登高山', '桃李争春', '暖春天地宽']
# sentenses = ['有志者事竟成，破釜沉舟，百二秦关终属楚']
# sentenses=['一二三四五六七']
sentenses = ['青山不墨千秋画', '两岸凉生菰叶雨', '无边落木萧萧下', '两只黄鹂鸣翠柳',
             '深秋帘幕千家雨', '月透柳帘窥案卷']
# sentenses = ['有志者事竟成，破釜沉舟，百二秦关终属楚']

def HMM(sentenses):
    with open(model_path + 'unigram.pkl', 'rb') as f:
        unigram = pickle.load(f)
    with open(model_path + 'transition.pkl', 'rb') as f:
        transition = pickle.load(f)
    with open(model_path + 'emit.pkl', 'rb') as f:
        emit = pickle.load(f)
    keep_size = 40
    model = MODEL_HMM(unigram, transition, emit, keep_size=keep_size)

    for sentense in sentenses:
        results = model.test(sentense)
        # print(sentense, results[0][0])
    return results[0][0]
if __name__ == '__main__':
    result_HMM=HMM(sentenses)
    print('最后一句的下联：',result_HMM)
