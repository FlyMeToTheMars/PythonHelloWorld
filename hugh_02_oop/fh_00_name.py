
# 类名一般用大驼峰命名法
"""
大驼峰命名法
1.每一个单词的首字母大写
2.单词与单词之间没有下划线

"""


# 定义一个对象
def demo():
    """
    这是一个测试函数
    :return:
    """
    print("hello python")


demo()

# 查看一个对象所有的方法
print(dir(demo()))
# 打印注释文档说明
print(demo.__doc__)
