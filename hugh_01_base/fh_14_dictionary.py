
# 字典
# 字典是无序的对象集合，列表是有序的对象集合
# 字典无序
# 键值对
# 值可以是任何数据类型，键只能使用字符串、数字或者元组
xiaoming = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75,
    "weight": 75.6,
}

print(xiaoming)
print(xiaoming["name"])

# 增加 / 修改
xiaoming["age"] = 10  # 如果这个值得没有的话，就会新建

# 删除 pop
xiaoming.pop("age")

# 合并字典 update
zidian = {"key": "value"}
zidian.update(xiaoming)
print(zidian)

# 清空 clear
zidian.clear()
print(zidian)

for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))

card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"},
]

for card_info in card_list:
    print(card_info)

# 字符串
# 单引号和双引号都能定义字符串 但是单引号不推荐

str1 = "hello python"
print(str1[0])
for k in str1:
    print(k)

# 统计长度
print(len(str1))

# 统计出现次数
print(str1.count("o"))

# 某个字符串出现的位置 (第一个字母出现的index)
print(str1.index("o"))

# Python对String提供的方法
# 判断是否只包含空格
# 判断是否有数字/单词/混合/每个单词首字母大写/大小写
# 查找和替换
# 针对句子的转换
poem = [
    "登黄鹤楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]

for poem_str in poem:
    print("|%s|" % poem_str.center(20, "\u3000"))  # 注意是中文空格

# 拆分 拼接 split join
# 常见使用： 按照index截取str

# linux的shebang #!  文件一开始加上这个
"""
#! /usr/bin/python3
"""

# id(变量) 查看变量地址

# Python可变类型和不可变类型
# 除了list和dict是可变类型，所有别的都是不可变类型，可以通过id()方法验证

# 如果想用方法修改全局变量，在方法里使用global关键字 + 全局变量名
# 如果不加的话会创建一个局部变量接收这个全局变量的值
# 全局变量必须定义在最上面  全局变量一般前面会加上g_ gl_这样的前缀
# 代码结构
"""
#!
import
全局变量
函数定义
执行代码
"""
