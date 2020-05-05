i = 0
# break
while i < 10:
    if i == 3:
        break

    print(i)

    i += 1

# continue
k = 0
while k < 10:
    if k == 3:

        # 下面的代码不添加上的话 k = 3 会一直执行下去
        k += 1

        continue

    print("k = %d" % k)

    k += 1

row = 1
while row <= 5:
    print("*" * row)
    row += 1

# print 默认换行，不换行的用法：
print("*", end="---")
print("*")

row_new = 1
while row_new <= 5:

    col = 1
    # 每一行要打印的星星和当前的行数一致
    while col <= row_new:
        # print("%d" % col)
        print("*", end="")
        col += 1

    # print("第 %d 行" % row_new)
    # 这行代码的目的是在一行代码的末尾增加一个换行
    print("")
    row_new += 1
