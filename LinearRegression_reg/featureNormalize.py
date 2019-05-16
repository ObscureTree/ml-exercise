import numpy as np

def feature_normalize(X):

    n = X.shape[1] # shape[1]返回特征矩阵的列数
    X_norm = X # 初始化特征缩放后的特征矩阵
    mu = np.zeros(n) # 初始化每一列特征的均值
    sigma = np.zeros(n) # 初始化每一列特征的标准差

    mu = np.mean(X)
    sigma = np.std(X)
    X_norm = (X_norm-mu)/sigma

    return X_norm, mu, sigma