# 目标函数
f = lambda x: (x**2-1)**2
e = 0.1       # 精度要求
a = 0           # 所求区间左边
b = 2          # 所求区间右边
## 只需改如下四个参数即可
f = lambda x: x**2 + 2*x
# 定义变量
e = 0.2       # 终止线
a = -3           # 左边
b = 5          # 右边


# 0.618法计算公式
lanb = lambda a, b : a + 0.382* (b -a)
mui = lambda a, b : a + 0.618* (b -a)

Mui = round(mui(a, b),3)
Mui_value = round(f(Mui), 3)

Lamb = round(lanb(a, b) ,3)
Lamb_value= round(f(Lamb), 3)

print(f'a={a} b={b}')
print(f'lanb:{Lamb}')
print(f'mui:{Mui}')
print(f'f(lanb)= {Lamb_value}')
print(f'f(mui)= {Mui_value}')
print()

while b - a > e: #判断是否到达迭代边界
    if Lamb_value < Mui_value:
        print('f(lanb) < f(mui)')
        print()
        b = Mui
        Mui = Lamb
        Lamb = round(lanb(a, b), 3)
    else:
        print('f(mui) < f(lanb) ')
        print()
        a = Lamb
        Lamb = Mui
        Mui = round(mui(a, b), 3)

    Mui_value = round(f(Mui), 3)
    Lamb_value = round(f(Lamb), 3)
    print(f'a={a} b={b}')
    print(f'lanb:{Lamb}')
    print(f'mui:{Mui}')
    print(f'f(lanb)= {Lamb_value}')
    print(f'f(mui)= {Mui_value}')


print(f'b-a绝对值为{abs(b -a)} 小于迭代边界 算法停止')
print(f'X包含于[{a}, {b}]')
print(f'X = {round((a + b)/ 2, 3)}')


#lanb = lambda a, b : a + 0.382* (b -a)
mui = lambda a, b : a + 0.618* (b -a)

Mui = round(mui(a, b),3)
Mui_value = round(f(Mui), 3)

Lamb = round(lanb(a, b) ,3)
Lamb_value= round(f(Lamb), 3)

print(f'a={a} b={b}')
print(f'lanb:{Lamb}')
print(f'mui:{Mui}')
print(f'f(lanb)= {Lamb_value}')
print(f'f(mui)= {Mui_value}')
print() #换行最后看着舒服

while b - a > e: #判断是否到达终止线
    if Lamb_value < Mui_value:
        print('f(lanb) < f(mui)')
        print()
        b = Mui
        Mui = Lamb
        Lamb = round(lanb(a, b), 3)
    else:
        print('f(mui) < f(lanb) ')
        print()
        a = Lamb
        Lamb = Mui
        Mui = round(mui(a, b), 3)

    Mui_value = round(f(Mui), 3)
    Lamb_value = round(f(Lamb), 3)
    print(f'a={a} b={b}')
    print(f'lanb:{Lamb}')
    print(f'mui:{Mui}')
    print(f'f(lanb)= {Lamb_value}')
    print(f'f(mui)= {Mui_value}')


print(f'b-a绝对值为{abs(b -a)} 小于终止线 算法停止')
print(f'X包含于[{a}, {b}]')
print(f'X = {round((a + b)/ 2, 3)}')
