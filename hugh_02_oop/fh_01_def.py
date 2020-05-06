class Cat:
    # 必须self开头 这边因为定义了@staticmethod 所以多余删除了
    @staticmethod
    def eat():
        print("小猫爱吃鱼")

    @staticmethod
    def drink():
        print("小猫要喝水")


# 创建对象
tom = Cat()
tom.eat()
tom.drink()

# 测试下来 () 不能省略

print(tom)
addr = id(tom)
# 十进制
print("%d" % addr)
# 十六进制
print("%x" % addr)

# 内置方法
"""
与__init__对应的，__del__方法，当对象从内存中销毁的时候会自动调用

__str__ 方法，相当于scala的toString
"""



