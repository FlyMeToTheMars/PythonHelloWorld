
"""
__new__
为对象分配空间
返回对象的引用

python获得了对象的引用后，将引用作为第一个参数，传递给__init__方法

重写__new__方法的代码非常固定 如下

"""


class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 为对象分配空间
        instance = super().__new__(cls)

        # 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)

"""
    单例：让类创建的对象，在系统中只哦与唯一的一个实例
"""
print("--------完整单例-------")


class SingleMusicPlayer(object):
    instance = None

    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1 判断类属性是否是空对象
        if cls.instance is None:
            # 2 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 1 判断是否执行过初始化动作
        if SingleMusicPlayer.init_flag:
            return

        # 如果没有初始化过
        print("初始化播放器")

        SingleMusicPlayer.init_flag = True


player1 = SingleMusicPlayer()
print(player1)

player2 = SingleMusicPlayer()
print(player2)
