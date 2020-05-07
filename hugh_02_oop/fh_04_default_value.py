
# 初始化
"""
__init__方法是专门用来定义一个类具有哪些属性的
"""


class Cat:

    # 设置默认值
    def __init__(self, new_name):
        print("初始化")

        # 属性
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

    # 必须返回字符串
    def __str__(self):
        # print("我是小猫 %s" % self.name) 错误示例
        return "我是小猫 %s" % self.name


# 使用累名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat("TomDemo")

# 可以用__init__方法内部使用self.属性名 = 属性的初始化值 就可以定义属性
# 定义属性之后，再使用Cat类创建的对象，都会拥有该属性
print(tom.name)
tom.eat()

# del 销毁是在一个python文件即将运行到结尾的时候
print(tom)

# Python 能够自动的将一堆括号内部的代码链接在一起

"""
身份运算符
is      is是判断两个标示符是不是引用同一个对象
is not  is not 是判断两个表示服是不是引用不用对象

is 与 == 的区别
is用于判断两个变量引用对象是否为同一个
==用于判断引用变量的值是否相等
"""