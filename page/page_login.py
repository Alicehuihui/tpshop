# 导包
import page
from base.base import Base
from base.get_logging import GetLogger

# 获取log日志器
log = GetLogger().get_logger()

class PageLogin(Base):
#     点击登录连接
    def page_click_login_link(self):
        log.info("[page_logging]执行:{}点击连接操作".format(page.login_link))
        self.base_click(page.login_link)
#     输入用户名
    def page_input_username(self,username):
        log.info("[page_logging]执行:{}元素，输入用户名：{}操作".format(page.login_username,username))
        self.base_input(page.login_username,username)
#     输入密码
    def page_input_password(self,password):
        log.info("[page_logging]执行:{}元素，输入密码：{}操作".format(page.login_password,password))
        self.base_input(page.login_password,password)
#     输入验证码
    def page_input_verify_code(self,code):
        log.info("[page_logging]执行:{}元素，输入验证码：{}操作".format(page.login_verify_code,code))
        self.base_input(page.login_verify_code,code)
#     点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)
#     获取异常信息
    def page_get_err_info(self):
        return self.base_get_text(page.login_err_info)
#     确认异常信息
    def page_err_info_ok(self):
        self.base_click(page.login_err_btn_info)
#     截图
    def page_get_image(self):
        log.info("[page_logging]执行:点击登录{}元素".format(page.login_btn))
        self.base_get_image()
#     安全退出
    def page_login_quit(self):
        self.base_if_exist(page.login_logout_link)
#     判断是否登录成功
    def page_if_login_success(self):
        return self.base_if_exist(page.login_logout_link)
#     判断是否退出成功
    def page_if_logout_success(self):
        return self.base_if_exist(page.login_link)
#     组合业务
    def page_login(self,username,password,code):
        log.info("[page_logging]正在执行登录操作，用户名：{} 密码：{}  验证码 {}".format(username,password,code))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verify_code(code)
        self.page_click_login_btn()

# 组合登录业务方法 给(购物车模块、订单模块、支付模块)依赖登录使用
    def page_login_success(self, username="13800001111", password="123456", code="8888"):
        # 点击登录连接
        self.page_click_login_link()
        log.info("[page_loging] 正在执行登录操作, 用户名：{} 密码：{}, 验证码:{}".format(username, password, code))
        # 调用 输入用户名
        self.page_input_username(username)
        # 调用 输入密码
        self.page_input_password(password)
        # 调用 输入验证码
        self.page_input_verify_code(code)
        # 调用 点击登录
        self.page_click_login_btn()