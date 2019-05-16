#!/usr/bin/env python
# coding: utf-8
import numpy as np

def normal_eqn(X, y):
    theta = np.zeros((X.shape[1], 1))
 
    theta=np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
 
 
    return theta