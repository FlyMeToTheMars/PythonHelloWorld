row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")

        col += 1

    print("")

    row += 1

# 制表
print("1\t2\t3")
print("10\t20\t30")
# 换行
print("hello\npython")
