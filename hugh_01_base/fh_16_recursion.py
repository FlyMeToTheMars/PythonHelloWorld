
# 递归


def sum_number(num):
    print(num)

    # 递归的出口
    if num == 1:
        return

    sum_number(num - 1)


sum_number(3)

# 递归在处理不确定的循环条件的时候会格外的有用。
# 比如 遍历整个文件目录结构
