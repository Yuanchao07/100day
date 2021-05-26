import time
# 定义数字类时钟


class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        """初始化
        :param hour:
        :param minute:
        :param second:
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        """走字"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# 创建时钟对象
clock = Clock(23, 50, 55)
while True:
    # 给时钟发消息读取时间
    print(clock.show())
    # 休眠1秒
    time.sleep(1)
    # 给时钟发消息走字
    clock.run()
