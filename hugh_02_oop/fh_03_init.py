
# 初始化
"""
__init__方法是专门用来定义一个类具有哪些属性的
"""


class Cat:

    def __init__(self):

        print("初始化")

        # 属性
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用累名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat()

# 可以用__init__方法内部使用self.属性名 = 属性的初始化值 就可以定义属性
# 定义属性之后，再使用Cat类创建的对象，都会拥有该属性
print(tom.name)
tom.eat()
