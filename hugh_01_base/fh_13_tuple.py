
# tuple 与列表类似，不同之处在于元祖的元素不能修改
# 元组一般用来存储不同类型的数据
# 定义的时候用的是 ()
info_tuple = ("zhangsan", 18, 1.75)
print(type(info_tuple))
print(info_tuple[0])
print("------遍历------")
for info_tuple in info_tuple:
    print(info_tuple)

# 创建空元组
empty_tuple = ()

# 格式化字符串后面的()本质上就是一个元组
tuple1 = ("小明", 21, 1.85)
str_tuple = "%s 年龄是 %d 身高是 %.2f" % tuple1
print("%s 年龄是 %d 身高是 %.2f" % tuple1)
print(str_tuple)

# tuple 和 list 中间是可以互相转换的
num_list = [1, 2, 3, 4]
type(num_list)
print(type(num_list))
num_tuple = tuple(num_list)
print(type(num_tuple))

print(list(num_tuple))
