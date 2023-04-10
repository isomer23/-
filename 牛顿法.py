from sympy import *
import numpy as np
# 定义符号
x1,x2 = symbols('x1, x2')
# 定义所求函数
f = 4*x1**2+x2**2-x1**2*x2
# 求解梯度值
def get_grad(f, X):
    # 计算一阶导数
    f1 = diff(f, x1)
    f2 = diff(f, x2)
    # 代入具体数值计算
    grad = np.array([[f1.subs([(x1, X[0]), (x2, X[1])])],
                   [f2.subs([(x1, X[0]), (x2, X[1])])]])
    return grad
# 求解Hession矩阵
def get_hess(f, X):
    # 计算二次偏导
    f1 = diff(f, x1)
    f2 = diff(f, x2)
    f11 = diff(f,x1,2)
    f22 = diff(f,x2,2)
    f12 = diff(f1,x2)
    f21 = diff(f2,x1)
    # 计算具体数值
    hess = np.array([[f11.subs([(x1,X[0]), (x2,X[1])]),
                        f12.subs([(x1,X[0]), (x2,X[1])])],

                        [f21.subs([(x1,X[0]), (x2,X[1])]),
                        f22.subs([(x1,X[0]), (x2,X[1])])]])
    hess = np.array(hess, dtype = 'float')
    return hess
# 牛顿迭代
def newton_iter(X0, err):
    # 记录迭代次数
    count = 0
    X1 = np.array([[0],[0]])
    while True:
        X2 = X0 - X1
        if sqrt(X2[0]**2 + X2[1]**2) <= err:
            break
        else:
            hess = get_hess(f, X0)
            # Hession矩阵的逆
            hess_inv = np.linalg.inv(hess)
            grad = get_grad(f, X0)
            X1 = X0
            # 迭代公式
            X0 = X1 - np.dot(hess_inv, grad)
            count += 1
            print('第',count,'次迭代:','x1=',X0[0],'x2=',X0[1])
    print('迭代次数为:',count)
    print('迭代结果为',X0)
# 设置初始点
X0 = np.array([[1],[1]])
err = 1e-3
newton_iter(X0, err)

