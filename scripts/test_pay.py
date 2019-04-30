# 导包
import unittest
from time import sleep
from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay


class TestPay(unittest.TestCase):
    def setUp(self):
        # 获取driver
        self.driver= GetDriver().get_driver()
        # 登录成功
        PageLogin(self.driver).page_login_success()
        sleep(2)
        # PayMoney类
        self.pay = PagePay(self.driver)
        # 回到首页
        self.pay.base_index()

    def tearDown(self):
        # 关闭driver
        GetDriver().quit_dirver()

    def test_pay(self):
        try:
            self.pay.page_pay()
            print("获取的支付结果",self.pay.page_payment_result())
            self.assertIn("订单提交成功",self.pay.page_payment_result())
        except Exception as e:
            self.pay.base_get_image()






