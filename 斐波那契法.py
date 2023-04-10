from sympy import *


def f(x):
    A = (x**2-1)**2
    return A


def Fabonaci_search(a,b,dx):
    N = (b-a)/dx

    F = [1, 1]
    while F[-1] < N:
        F.append(F[-2] + F[-1])
    print(F)

    n = len(F) - 1  # 获取斐波那契数列的长度(计数从0开始）
    if n < 3:
        print("精度过低，无法进行斐波那契一维搜索")
    else:
        pass

    x_values = []
    x_values.append(a)
    x_values.append(b)
    x1 = a + F[n - 2] / F[n] * (b - a)
    x2 = a + F[n - 1] / F[n] * (b - a)
    t = n
    i = 0
    while (t > 3):
        i += 1
        if f(x1) < f(x2):  # 如果f(x1)<f(x2)，则在区间(x1,b)内搜索
            a = x1
            x1 = x2
            x2 = a + F[t - 1] / F[t] * (b - a)
        elif f(x1) > f(x2):  # 如果f(x1)>f(x2),则在区间(a,x2)内搜索
            b = x2
            x2 = x1
            x1 = a + F[t - 2] / F[t] * (b - a)
        else:  # 如果f(x1)=f(x2)，则在区间(x1,x2)内搜索
            a = x1
            b = x2
            x1 = a + F[t - 2] / F[t] * (b - a)
            x2 = a + F[t - 1] / F[t] * (b - a)
        t -= 1
        x_values.append(a)
        x_values.append(x1)
        x_values.append(x2)
        x_values.append(b)
    #当t<3时
    x1 = a + 0.5 * (b - a)  # 斐波那契数列第3项和第2项的比
    x2 = x1 + 0.1 * (b - a)  # 偏离一定距离，人工构造的点
    if f(x1) < f(x2):  # 如果f(x1)<f(x2)，则在区间(x1,b)内搜索
        a = x1
    elif f(x1) > f(x2):  # 如果f(x1)>f(x2),则在区间(a,x2)内搜索
        b = x2
    else:  # 如果f(x1)=f(x2)，则在区间(x1,x2)内搜索
        a = x1
        b = x2
    x_values.append(a)
    x_values.append(x1)
    x_values.append(x2)
    x_values.append(b)
    print(f'迭代第{i}次,迭代精度小于等于{dx}，最终的搜索区间为：{min(a, b), max(a, b)}')
    print(f'A的最小值：{f((a + b) / 2)}')
    print('确定最大值的两端值为：', f(a), f(b))



if __name__ == '__main__':
    a = 0  # 区间左端点
    b = 2  # 区间右端点
    dx = 0.1  # 迭代精度

    Fabonaci_search(a, b, dx)