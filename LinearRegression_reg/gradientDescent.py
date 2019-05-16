#!/usr/bin/env python
# coding: utf-8

import numpy as np
from computeCost import *

def gradient_descent(X, y, theta, alpha, num_iters):

    m = y.size
    J_history = np.zeros(num_iters) # 每一次迭代产生一个代价函数

    for i in range(0, num_iters):
        theta = theta-(alpha/m)*(h(X,theta)-y).dot(X)
        J_history[i] = compute_cost(X,y,theta) # 每一次迭代产生的theta来计算代价函数值

    return theta, J_history