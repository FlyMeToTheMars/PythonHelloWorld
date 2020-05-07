
class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


wangcai = Animal()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()


# 子类拥有父类的所有方法
class Dog(Animal):

    def bark(self):
        print("汪汪叫")


wangwang = Dog()

wangwang.eat()
wangwang.drink()
wangwang.run()
wangwang.sleep()
wangwang.bark()


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):

        print("我是啸天犬")

        super().bark()
        # Python2.0 如果要实现上面的功能，有点复杂 代码如下
        """
        Dog.bark(self)
        """

        print("aafsdwaerwgybds")


# 有没有括号 对Python来说 说法很大
xtq = XiaoTianQuan()
xtq.bark()


class A:
    # 属性在init方法中定义
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):

        # 在子类的对象方法中不能访问父类的私有属性和方法
        # 但是可以通过调用父类的共有方法间接调用父类的公有属性和方法
        print("访问父类的私有属性 %d" % self.__num2)


b = B()
print(b)
"""
在外界不能直接访问对象的私有属性，调用方法
print(b.__num2)
b.__test()
"""
print(b.num1)


class C:

    def test(self):
        print("test 方法")


class D:

    def demo(self):
        print("demo 方法")


# 多继承
class E(C, D):

    pass


# 创建子类对象
e = E()
e.test()
e.demo()

# 应该避免两个父类汇总存在同名的属性和方法
"""
python中多继承两个父类出现相同的方法 属性名的时候
使用MRO选择执行顺序的
"""
print(E.__mro__)

"""
新式类 以Object为基类的对象
旧式类 不以Object为基类的对象
两者在多继承时 会影响到方法的搜索顺序
"""
