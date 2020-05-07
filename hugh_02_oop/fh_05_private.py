
# 私有
class Woman:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("%s 的年龄是 %d" %
              (self.name,
               self.__age))


xiaofang = Woman("小芳")
# 私有属性不能直接调用 但是Python中没有真正的私有属性和方法 可以使用下面第二行的代码调用
# print(xiaofang.__age)
print(xiaofang._Woman__age)
xiaofang.secret()
