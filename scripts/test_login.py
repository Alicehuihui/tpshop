# 导包
import unittest
from time import sleep
from parameterized import parameterized
from base.get_driver import GetDriver
from page.page_login import PageLogin
from tool.read_txt import read_txt
from base.get_logging import GetLogger

# 获取log日志器
log = GetLogger().get_logger()

# 新建测试类并继承
def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[2:]

class TestLogin(unittest.TestCase):
    # login = None
    @classmethod
    def setUpClass(cls):
        try:
            # 实例化获取页面对象PageLogin
            cls.login = PageLogin(GetDriver().get_driver())
            # 点击登录连接
            cls.login.page_click_login_link()
        except Exception as e:
            log.error("错误：{}".format(e))
            cls.login.base_get_image()

    @classmethod
    def tearDownClass(cls):
    # 关闭driver驱动对象
        GetDriver().quit_dirver()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self,username,password,code,expect_result,status):
        try:
            # 调用登录方法
            self.login.page_login(username,password,code)
            # 判断是否为正项用例
            if status == "ture":
                try:
                    # 断言是否登录成功
                    self.assertTrue(self.login.page_if_login_success())
                except Exception as e :
                    # 截图
                    self.login.base_get_image()
                    log.error("错误：{}".format(e))
                    # 安全退出
                self.login.page_login_quit()
                    # 点击登录连接
                self.login.page_click_login_link()

            else:
            # 获取登录提示信息
                msg = self.login.page_get_err_info()
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    # 截图
                    log.error("错误：{}".format(e))
                    # 点击确认框
                self.login.page_err_info_ok()

        except Exception as e:
            log.error("错误：{}".format(e))
            # 截图
            self.login.base_get_image()