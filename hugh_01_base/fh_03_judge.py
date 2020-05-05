# else if
holiday_name = "情人节"

if holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")

elif holiday_name == "平安夜":
    print("买苹果")
    print("吃大餐")

# 增加判断条件
elif holiday_name == "生日":
    print("买蛋糕")

else:
    print("每天都是节日啊")

# if 嵌套
has_ticket = True

knife_length = 30
if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length > 20:
        print("您鞋携带的刀太长了，有 %d 公分" % knife_length)
        print("不允许上车")

    else:
        print("安检通过")



else:
    print("大哥，请先买票")

