# 程序的三大流程 顺序结构、选择结构、循环结构
i = 1
while i <= 5:
    print("Hello Python")

    i = i + 1

print("循环结束后， i = %d" % i)

# 赋值运算符 assigning operator
# +
# +=
# -=
# *=
# /=
# //=
# %=
# **=

k = 0
result = 0
# 累加
while k <= 100:
    print("k = %d" % k)
    print("result的结果 %d" % result)

    result += k

    k += 1

print("0 到 100 数字求和结果是 %d" % result)


