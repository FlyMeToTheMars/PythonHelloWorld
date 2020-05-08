
"""
try:
    尝试执行的代码
except:
    出现错误的处理
"""

try:
    num = int(input("请输入一个整数："))

    result = 8 / num

    print(result)

except ZeroDivisionError:
    # 错误的处理代码
    print("请输入正确的整数")
except ValueError:
    print("请输入正确的整数")
#     捕获未知错误
except Exception as result:
    print("未知错误 %s" % result)
else:
    # 没有异常的时候才会执行的
    print("尝试成功")
finally:
    # 总是会执行的代码
    print("总是会执行")

print("-" * 50)


"""
异常的传递
python 会把异常一直向上传递
"""


def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


print(demo2())


def input_password():

    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码成都 >= 8 , 返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")

    # 创建异常对象
    ex = Exception("密码长度不够")

    # 主动抛出异常
    raise ex


print(input_password())
