
"""
python操作文件

open 打开文件 返回文件对象
read 文件内容读取到内存
write 将内容写入文件
close 关闭文件

文件指针
open()方法有两个参数 第二个参数制定的是打开的方式
存在r w a r+ w+ a+这些方式 用str格式传入

readline 按行读取
"""


"""
小文件复制
file_read = open("README")
file_write = open("README[复件]","w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()


复制大文件 用readline
"""

"""
倒入 import os
rename 重命名
remove 删除

listdir 目录列表
mkdir 创建目录
rmdir 删除目录
getcwd 获取当前目录
chdir 修改工作目录
path.isdir 判断是否是文件
"""

"""
python2.x 默认ASCII编码
    python2 使用 
    # *-* coding:utf-8 *-*
    来指定编码格式
python3.x 默认使用UTF-8

"""