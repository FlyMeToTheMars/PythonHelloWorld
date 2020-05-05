import keyword

"""
列表（别的编程语言 一般叫数组）
"""
name_list = ["zs", "ls", "ww"]
print(name_list[2])

# 修改
name_list[2] = "aa"
print(name_list[2])
print(name_list.index("aa"))

# 增加
name_list.append("王小二")
name_list.insert(1, "nice")

temp_list = ["孙悟空", "猪八戒"]
# 可以把其他列表中的完整内容追加到当前列表末尾
name_list.extend(temp_list)

print(name_list)

# 删除
# remove
name_list.remove("ls")
print(name_list)

# 默认删除最后一个数据
name_list.pop()
print(name_list)

# 指定索引可以删除
name_list.pop(3)
print(name_list)

# len 长度
list_len = len(name_list)
print(list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("zs")
print("张三出现了 %d 次" % count)

# 排序
# 升序
name_list.sort()
print("排序")
print(name_list)

# 降序
name_list.sort(reverse=True)
print(name_list)

# 逆序（反转） 把列表中的顺序完全翻转
name_list.reverse()
print(name_list)

# clear 清空列表
name_list.clear()
print(name_list)

# del 关键字 本质上是用来讲一个变量从内存中删除,后续就不能再使用了
# 日常开发中使用得不多
name = "小明"
del name
print(name)
