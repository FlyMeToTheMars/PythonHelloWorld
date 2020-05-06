
class Cat:
    # 必须self开头
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    # 可以通过self.来调用对象的属性或者其他对象的方法
    def drink(self):
        print("%s 要喝水" % self.name)


# 创建对象
tom = Cat()
# 不推荐使用 给某个对象添加了属性 在外部
tom.name = "Tom"
tom.eat()
tom.drink()

# 测试下来 () 不能省略

print(tom)
addr = id(tom)
# 十进制
print("%d" % addr)
# 十六进制
print("%x" % addr)
