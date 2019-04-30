# 导包
from selenium import webdriver
import page

class GetDriver:
#     设置类属性
    driver = None
    @classmethod
#     获取driver
    def get_driver(cls):
        if cls.driver is None:
#         实例化浏览器
            cls.driver = webdriver.Firefox()
#         最大化浏览器
            cls.driver.maximize_window()
#         打开浏览器
            cls.driver.get(page.url)
        return cls.driver

#     退出driver
    @classmethod
    def quit_dirver(cls):
        if cls.driver :
            cls.driver.quit()
            cls.driver = None
# 自测
if __name__ == '__main__':
    # 第一次获取浏览器
    print(GetDriver().get_driver())
# 第二次获取浏览器
    print(GetDriver().get_driver())
# 调用关闭，测试关闭后driver是否为None
    GetDriver().quit_dirver()