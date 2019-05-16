#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt

def plot_data(x, y):
    
    plt.scatter(x,y,marker='o',c='b')
    plt.xlabel('population')
    plt.ylabel('profites')


