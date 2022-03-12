#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shiyu Huang
# @File    : demo_lstm.py

import tensorflow as tf
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
# print(tf.__version__)    #查看tensorflow版本

import model_lstm as model
import sys
import os

import dataflow


def LSTM(sentenses):
    # sentenses = ['青山不墨千秋画', '两岸凉生菰叶雨', '无边落木萧萧下', '两只黄鹂鸣翠柳',
    #              '深秋帘幕千家雨', '月透柳帘窥案卷']
    # sentenses = ['有志者事竟成，破釜沉舟，百二秦关终属楚']

    tf.reset_default_graph()

    # print('loading model...')
    in_seq_holder = tf.placeholder(tf.int32, shape=[1, None], name='in_seq')
    in_seq_len_holder = tf.placeholder(tf.int32, shape=[1], name='in_seq_len')
    test_model = model.Seq2Seq()
    vocabs = dataflow.read_vocab(dataflow.vocabular)
    vocab_indices = dict((c, i) for i, c in
                         enumerate(vocabs))
    voc_size = len(vocabs)
    test_model.build_infer(in_seq_holder, in_seq_len_holder,
                           voc_size,
                           dataflow.hidden_unit, dataflow.layers, name_scope='infer')

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    sess.run(tf.global_variables_initializer())
    saver = model.Saver(sess)
    saver.load(dataflow.init_path, scope_name='infer', del_scope=True)

    # print('testing...')

    for sentense in sentenses:
        new_sentense = []
        for v in sentense:
            new_sentense.append(v)
        new_sentense.append('</s>')
        in_seq = dataflow.encode_text(new_sentense, vocab_indices)
        in_seq_len = len(in_seq)
        outputs = sess.run(test_model.infer_output,
                           feed_dict={
                               in_seq_holder: [in_seq],
                               in_seq_len_holder: [in_seq_len]})
        output = outputs[0]
        output = dataflow.decode_text(output, vocabs)
        output = ''.join(output.split(' '))
        # print(sentense, output)
    return output


if __name__ == '__main__':
    sentense1 = ['有志者事竟成，破釜沉舟，百二秦关终属楚']
    sentense2 = ['有志者事竟成，破釜沉舟，百二秦关终属楚']
    result1=LSTM(sentense1)
    print('第一个已经完成！')
    result2=LSTM(sentense2)
    print(result1,result2)

