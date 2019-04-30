# 导包
import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder
from scripts.test_login import log

# 新建测试类并继承
class TestOrder(unittest.TestCase):
    # setUp
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 调用登录PageLoge对象中，登录方法
        PageLogin(self.driver).page_login_success()
        # 实例化PageOrder
        self.order = PageOrder(self.driver)
        sleep(3)
        # 回到首页
        self.order.page_click_index()

    # tearDown
    def TearDown(self):
        # 关闭driver
        GetDriver().quit_dirver()
    def testorder(self):
        try:
            # 调用 下订单业务方法
            self.order.page_order()
            # 断言
            msg = self.order.page_get_order_result()
            print("msg:",msg)
            self.assertIn("提交成功",msg)
        except Exception as e:
            # 截图
            self.order.base_get_image()
            # 日志
            log.error(e)