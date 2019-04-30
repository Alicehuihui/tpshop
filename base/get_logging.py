# 导包
import logging.handlers

class GetLogger:
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器控制台
            sh = logging.StreamHandler()
            # 获取处理器文件—时间分割
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/log02.log",when="midnight",interval=1,backupCount=30,encoding="utf-8")
            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到处理器 文件
            th.setFormatter(fm)
            # 将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        # 返回日志器
        return cls.logger