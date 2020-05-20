from wxpy import *

# 初始化一个机器人对象
# cache_path缓存路径，给定值为第一次登录生成的缓存文件路径
bot = Bot()
#获取好友列表(包括自己)
my_friends = bot.friends(update=False)

print(my_friends.stats_text())
