# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         condition_test
# Description:  
# Author:       Allen
# Time:         2020/12/20 10:50
# ------------------------------------------------------------------------------
# 条件变量，用于复杂的线程间同步
import threading


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super(XiaoAi, self).__init__(name='小爱')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
            self.cond.wait()
            print("{} : {}".format(self.name, "在"))
            self.cond.notify()

            self.cond.wait()
            print("{} : {}".format(self.name, "fine"))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super(TianMao, self).__init__(name='天猫精灵')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
            print("{} : {}".format(self.name, "小爱同学"))
            self.cond.notify()
            self.cond.wait()

            print("{} : {}".format(self.name, "how are you"))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    cond = threading.Condition()
    xiao_ai = XiaoAi(cond)
    tian_mao = TianMao(cond)

    # 启动方法很重要
    # 在调用with cond 之后才能调用wait或者notify方法
    # condition有两层锁，一把底层锁会在线程调用了wait方法的时候释放，上面的锁会在每次调用wait的时候分配一把锁并放入到cond的等待对列中，等待notify方法的唤醒
    xiao_ai.start()
    tian_mao.start()
