import keyword
print(keyword.kwlist)

# 单词与单词之间用_分割

# 驼峰命名法

"""
    IF
"""
# Tab和空格不能混用

age = 24
if age >= 18:
    print("你已经成年")
    print("IDEA默认是空格")
else:
    print("不符合需求")
# IF 代码块

if age >= 0 or age <= 120:
    print("年龄正确")

if age >= 0 and age <= 120:
    print("年龄正确")

# 判断