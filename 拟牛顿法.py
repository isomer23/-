
import numpy as np
from sympy import symbols

x1 = symbols("x1")
x2 = symbols("x2")


def jacobian(f, x):

    grandient = np.array([400 * x[0] * (x[0] ** 2 - x[1]) + 2 * (x[0] - 1), -200 * (x[0] ** 2 - x[1])], dtype=float)
    return grandient


def dfp_newton(f, x, iters):
    # 步长
    learning_rate = 1

    G = np.eye(2)
    x_len = x.shape[0]

    epsilon = 1e-5
    for i in range(1, iters):
        g = jacobian(f, x)
        if np.linalg.norm(g) < epsilon:
            break
        p = np.dot(G, g)
        # 更新x值
        x_new = x - p * learning_rate
        print("第" + str(i) + "次迭代后的结果为:", x_new)
        g_new = jacobian(f, x_new)
        y = g_new - g
        k = x_new - x
        Gy = np.dot(G, y)
        y_t_G = np.dot(y, G)
        yGy = np.dot(np.dot(y, G), y)
        # 更新G正定矩阵
        G = G + k.reshape([x_len, 1]) * k / np.dot(k, y) - Gy.reshape([x_len, 1]) * y_t_G / yGy
        x = x_new
    return x


if __name__ == "__main__":
    x = np.array([1, 9], dtype=float)
    f = 100 * (x1 ** 2 - x2 ** 2) ** 2 + (x1 - 1) ** 2
    # print(bfgs_newton(f, x, 2000))
    print(dfp_newton(f, x, 1000))