
"""
发布
固定模版：

from distutils.core import setup

# 多值的字典参数，setup是一个函数
setup(name="Hello",  # 包名
      version="1.0",  # 版本
      description="a simple example",  # 描述信息
      long_description="简单的模块发布例子",  # 完整描述信息
      author="FlyHugh",  # 作者
      author_email="flyhobo@live.com",  # 作者邮箱
      url="flymetothemars.github.io",  # 主页
      py_modules=["hello.request",
                  "hello.response"])  # 记录包中包中包含的所有模块
"""

"""
第二步
构建
python3 setup.py build
"""

"""
第三步
python3 setup.py sdist
"""

"""
安装
tar zxvf 解压
sudo python3 setup.py install

然后打开python3运行即可

"""

