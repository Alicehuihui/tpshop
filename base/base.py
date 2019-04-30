# 导包
import time
from selenium.webdriver.support.wait import WebDriverWait
import page
from base.get_logging import GetLogger

# 获取log日志器
log = GetLogger().get_logger()

class Base:

    def __init__(self, driver):
        log.info("[base]:正在获取初始driver对象：{}".format(driver))
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("[base]:正在查找{}元素，默认定位超时时间为：{}".format(loc,timeout))
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        log.info("[base]:正在对{}元素实行点击事件".format(loc))
        self.base_find_element(loc).click()

    # 输入元素方法
    def base_input(self,loc,value):
        log.info("[base]:正在输入{}元素，".format(loc))
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本信息
    def base_get_text(self,loc):
        log.info("[base]:正在获取{}文本".format(loc))
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        log.info("[base]:断言出错，调用截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info("[base]:{}元素查找成功，存在页面".format(loc))
            # 找到元素
            return True
        except:
            log.info("[base]:{}元素查找失败，不存在页面".format(loc))
            return False
    # 回到首(页购物车、下订单、支付)都需要用到此方法
    def base_index(self):
        self.driver.get(page.url)

    # 切换frame表单方法
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()
    # 窗口切换
    def base_switch_to_window(self,title):
        self.base_get_title_handle(title)

    # 获取指定title页面的handle方法
    def base_get_title_handle(self,title):
    #     获取当前页面所有的handles
        for handle in self.driver.window_handles:
    #     切换handle
            self.driver.switch_to.window(handle)
    #     获取当前页面title并判断是否等于指定参数title
            if self.driver.title == title:
        # 返回handle
                return handle