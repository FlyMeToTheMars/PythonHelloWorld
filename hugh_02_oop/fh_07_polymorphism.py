
# 多态
"""
不同的子类对象调用相同的父类方法，产生不同的执行结果
多态可以增加代码的灵活度
以继承和重写父类方法为前提
是调用方法的技巧，不回影响到类的内部设计
"""


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍。。。" % self.name)


class XiaoTianQuan(Dog):

    def game(self):
        print("%s 飞到天上去玩耍。。。" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))

        dog.game()


wangcai = Dog("旺财")
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)

wangcai_1 = XiaoTianQuan("wangcai")
xiaoming_1 = Person("xiaoming")
xiaoming_1.game_with_dog(wangcai_1)
