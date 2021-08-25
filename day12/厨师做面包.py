'''
    三个厨师做面包 每人三秒做1个面包,做完放到框里，框最大能放500个,框满了停3秒在造
    五个客人买面包 每个面包2元 每人都有1000元
    若篮子里没面包了，等两秒钟，然后再买


'''

import threading
import time
miaobao = 0
class chushi(threading.Thread):
    cname = ""
    gname = ""
    money = 0
    count = 0
    a = 0
    def run(self) -> None:
        global miaobao
        while True:
            if self.cname:
                if miaobao < 500:
                    miaobao = miaobao+1
                    self.a = self.a + 1
                    print("厨师", self.cname, "做了", self.a, "个面包")
                if miaobao >= 500:
                    print("满了")
                    time.sleep(2)
                if miaobao == 500:
                    print("存满了！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！1")
                    break
            elif self.gname:
                if miaobao >= 1:
                    if self.money > 1:
                        self.money = self.money - 3
                        miaobao = miaobao - 1
                        self.count = self.count + 1
                        print(self.gname,"一共买了",self.count,"个面包！")
                    elif self.money <= 2:
                        break
                elif miaobao == 0:
                    print("稍等！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
                    time.sleep(2)


chushi1 = chushi()
chushi2 = chushi()
chushi3 = chushi()
chushi4 = chushi()
chushi5 = chushi()
chushi6 = chushi()
chushi1.cname = "c001"
chushi2.cname = "c002"
chushi3.cname = "c003"
chushi1.gname = "g001"
chushi1.money = 3000
chushi2.gname = "g002"
chushi2.money = 3000
chushi3.gname = "g003"
chushi3.money = 3000
chushi4.gname = "g004"
chushi4.money = 3000
chushi5.gname = "g005"
chushi5.money = 3000
chushi6.gname = "g006"
chushi6.money = 3000
chushi1.start()
chushi2.start()
chushi3.start()
chushi4.start()
chushi5.start()
chushi6.start()

