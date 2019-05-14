#!/usr/bin/env python
# coding: utf-8

import numpy as np

def h(X, theta):
    return X.dot(theta)
    
def compute_cost(X, y, theta):

    m = y.size # 样本数
    cost = 0 # 初始化代价函数值
    myh = h(X,theta) # 假设函数值
    
    cost = (myh-y).dot(myh-y)/(2*m) # 计算代价函数
    
    return cost