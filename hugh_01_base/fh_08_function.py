def multiple_table():

    # Code
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="\t")

            col += 1

        print("")

        row += 1

# 第二个fun 提示声明函数上方需要有两个空行 方法注释写在方法名下方的"""里面"""


def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


say_hello()


def sum_2_sum(num1, num2):
    """

    :param num1: 第一个求和的数字
    :param num2: 第二个求和的数字
    :return: 返回值
    """
    # num1 = 10
    # num2 = 20

    result = num1 + num2

    print("%d + %d = %d" % (num1, num2, result))


sum_2_sum(10, 30)

# 参数 实参 形参


def sum_2_sum_2(num1, num2):
    """对两个数字的求和"""
    # 可以使用返回值 告诉调用函数一方的结果
    result1 = num1 + num2

    return result1


sum_result = sum_2_sum_2(10, 20)
print(sum_result)

# 嵌套调用


def test1():
    print("*" * 50)


def test2():
    """

    """
    print("-" * 50)

    test1()


test2()

# 关键字、函数和方法
# 关键字是Python内置的，具有特殊意义的标识符 使用的时候不需要加括号
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# 函数封装了独立的功能，可以直接调用

# 函数名(参数)

# 对象.方法名

# python内置函数 容器通用
# len 长度 元素个数
# del 删除变量 del() 两种使用方式 效果一样
# max min 如果是字典，只针对key比较
# cmp(a, b) 比较两个值，-1小于/0 相等 /1 大于, Python 3.X 取消了cmp函数

# 列表和tuple都可以用+ 和 *，字典比较特殊
# List用extends相当于flatmap了，使用append相当于添加一个新元素
# in/not in


def measure():
    """测量温度和湿度

    :return:
    """
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 返回值里面的()可以省略
    return temp, wetness


result = measure()
print(result)

