import numpy as np
from sympy import *
import math
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
x1, x2, t = symbols('x1, x2, t')
def func():
    # 目标函数
    return 2*x1**2+x2**2
def grad(data):
    # 求梯度向量,data=[data1, data2]
    f = func()
    grad_vec = [diff(f, x1), diff(f, x2)]  # 求偏导数,梯度向量
    grad = []
    for item in grad_vec:
        grad.append(item.subs(x1, data[0]).subs(x2, data[1]))
    return grad
def grad_len(grad):
    # 梯度向量的模长
    vec_len = math.sqrt(pow(grad[0], 2) + pow(grad[1], 2))
    return vec_len
def zhudian(f):
    # 求得min(t)的驻点，即求步长
    t_diff = diff(f)
    t_min = solve(t_diff)
    return t_min
def main(X0, theta):
    f = func()
    grad_vec = grad(X0)
    grad_length = grad_len(grad_vec)  # 梯度向量的模长
    k = 0
    data_x = [0]
    data_y = [0]
    while grad_length > theta:  # 迭代的终止条件
        k += 1
        p = -np.array(grad_vec)
        # 迭代
        X = np.array(X0) + t*p
        t_func = f.subs(x1, X[0]).subs(x2, X[1])
        t_min = zhudian(t_func)
        X0 = np.array(X0) + t_min*p
        grad_vec = grad(X0)
        grad_length = grad_len(grad_vec)
        print('grad_length', grad_length)
        print('坐标', X0[0], X0[1])
        data_x.append(X0[0])
        data_y.append(X0[1])

    print(k)
main([1, 1], 0.1)