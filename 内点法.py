"""
内点法
python库sympy中集成了许多用于计算一阶导数和二阶导数的函数
"""
from sympy import *

# 定义变量
x1, x2, t = symbols('x1 x2 t')

# 定义目标函数
func = x1+x2
funr = x1+x2-t*log(-(x1**2)+x2)-t*log(x1)
# 求导
de_x1 = diff(funr, x1, 1)  # 对x1求一阶导
de_x2 = diff(funr, x2, 1)  # 对x2求一阶导
print(de_x1)
print(de_x2)
# de_x1_x1 = diff(func, x1, x1)  # 对x1和x1求二阶导
# de_x1_x2 = diff(func, x1, x2)  # 对x1和x2求二阶导
# de_x2_x1 = diff(func, x2, x1)  # 对x2和x1求二阶导
de_x2_x2 = diff(func, x2, x2)  # 对x2和x2求二阶导

