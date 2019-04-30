import unittest
import time
from tool.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("./")
# 生成报告目录及文件名称
dir_path = "../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 获取文件流并调用run运行
with open(dir_path, "wb") as f:
    HTMLTestRunner(stream=f, title="Tpshop商城自动化测试报告", description="操作系统：win7").run(suite)





