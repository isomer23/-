
from sympy import *

# 设置变量
x1 = symbols("x1")
x2 = symbols("x2")
alpha = symbols("alpha")


# 构造拉格朗日等式
L = 2*x1**2+x2**2+x1*x2-x1-x2 - alpha * (x1 + x2 - 1)

# 求导，构造KT条件
difyL_x1 = diff(L, x1)  # 对x1求偏导
difyL_x2 = diff(L, x2)  # 对x2求偏导
difyL_alpha = diff(L, alpha)  # 对alpha求导

# 求解KT等式
aa = solve([difyL_x1, difyL_x2, difyL_alpha], [x1, x2, alpha])
print(aa)
x1 = aa.get(x1)
x2 = aa.get(x2)
alpha = aa.get(alpha)
print("最优解为：", 2*x1**2+x2**2+x1*x2-x1-x2 - alpha * (x1 + x2 - 1))

