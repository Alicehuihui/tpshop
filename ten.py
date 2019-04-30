# from time import sleep
# from selenium import webdriver

# 26. 需求：对《注册A.html》进行信息注册
# 账号：admin,密码：123456，电话：18600000000，电子邮件：123@qq.com 要求：
# 1. 定位方式统一使用CSS定位
# 2. 暂停2秒钟点击注册用户A按钮
# 3. 暂停3秒钟后关闭浏览器
# 导包
# from time import sleep
# from selenium import webdriver
#
# class reg_a ():
#     driver = webdriver.Firefox()
#     url = "file:///C:/Users/Administrator/Desktop/%E6%B3%A8%E5%86%8CA.html"
#     driver.get(url)
#     driver.maximize_window()
#     driver.find_element_by_css_selector("#userA").send_keys("admin")
#     driver.find_element_by_css_selector("#passwordA").send_keys("123456")
#     driver.find_element_by_css_selector("#telA").send_keys("18600000000")
#     driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
#     sleep(2)
#     driver.find_element_by_css_selector("#zc>fieldset>button").click()
#     sleep(3)
#     driver.quit()


# 27.需求：对《注册实例.html》进行信息注册
# 账号：admin,密码：123456，电话：18600000000，电子邮件：123@qq.com 要求：
#     1. 对注册《主界面、注册A、注册B》三个注册信息进行注册信息填写
#     2. 定位方式不限
#     3. 暂停3秒钟关闭浏览器
# from time import sleep
# from selenium import webdriver
#
# class reg ():
#     # 开始
#     # def start(self):
#     driver = webdriver.Firefox()
#     url = "file:///C:/Users/Administrator/Desktop/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
#     driver.get(url)
#     driver.maximize_window()
#
#     # 注册实例
#     # def reg_in(self):
#     driver.find_element_by_css_selector("#user").send_keys("admin")
#     driver.find_element_by_css_selector("#password").send_keys("123456")
#     driver.find_element_by_css_selector("#tel").send_keys("18600000000")
#     driver.find_element_by_css_selector("#email").send_keys("123@qq.com")
#
#
#     # # 注册A
#     # def reg_a(self):
#     driver.switch_to.frame("idframe1")
#     driver.find_element_by_css_selector("#userA").send_keys("admin")
#     driver.find_element_by_css_selector("#passwordA").send_keys("123456")
#     driver.find_element_by_css_selector("#telA").send_keys("18600000000")
#     driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
#     #
#     #
#     # # 注册B
#     # def reg_b(self):
#     driver.switch_to.default_content()
#     driver.switch_to.frame("myframe2")
#     driver.find_element_by_css_selector("#userB").send_keys("admin")
#     driver.find_element_by_css_selector("#passwordB").send_keys("123456")
#     driver.find_element_by_css_selector("#telB").send_keys("18600000000")
#     driver.find_element_by_css_selector("#emailB").send_keys("123@qq.com")
#     #
#     # # 关闭浏览器
#     # def end(self):
#     sleep(3)
#     driver.quit()



# 28需求：对TPshop/iweb_shop项目进行前台登录设计脚本
# 要求：
# 1. 使用unittest框架
# 2. 使用Fixture(setup、tearDown)
# 3. 浏览器最大化、隐式等待30秒
# 4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5. 图片命名格式为脚本执行时间
#
# 导包
import unittest
from time import sleep
import time
from selenium import webdriver


class Tpshop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://www.tpshop.com/index.php"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_partial_link_text("登录").click()

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def login(self):
        try:
            self.driver.find_element_by_css_selector("#username").send_keys("admin")

        except :
            self.driver.get_screenshot_as_file("../image/{}.png".format(
                time.strftime("%Y_%m_%d %H_%M_%S"))


