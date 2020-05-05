
name_list = ["张三", "李四", "王五", "王小二"]

# 使用迭代遍历列表
for my_name in name_list:
    print("我的名字叫 %s " % my_name)

# python 的列表中可以存储不用类型的数据，但是一般不这么用

# 完整的for循环
"""
for 变量 in 集合:
    循环体代码
else: 
    没有通过break 退出循环，循环结束后，会执行的代码
    如果for循环是通过break退出的，就不会执行
"""
for num in [1, 2, 3]:
    print(num)

    if num == 2:
        break
else:
    print("会执行吗？")

print("循环结束")

# 使用场景：
for num in [1, 2, 3]:
    # TODO 提示注释
    pass  # 占位符
