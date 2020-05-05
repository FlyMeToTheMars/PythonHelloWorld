import random

player = int(input("请输入您要出的拳 石头输入1，剪刀输入2，布输入3:"))

computer = random(1, 3)

print("玩家选择的拳头是： %d - 电脑出的拳头是 %d" % (player, computer))

# 比较胜负
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("恭喜玩家胜利")
elif player == computer:
    print("真是心有灵犀，平局")
else:
    print("电脑获胜")
