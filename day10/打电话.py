#定义一个空调类和对应的测试类
class kongtiao:
    __pinpai = ""
    __money = None
    def setpinpai(self,pinpai):
        self.__pinpai = pinpai
    def getpinpai(self):
        return self.__pinpai
    def setmoney(self,money):
        if money > 0:
            self.__money = money
        elif money <= 0:
            print("价格错误！")
        else:
            print("输入非法！！！！！！！！！！！！！！！！！")
    def getmoney(self):
        return self.__money
    def kaiji(self):
        print("空调开机了！")
    def guanji(self,fenzhong):
        print("空调将在",int(fenzhong),"分钟后自动关闭。")
    def jieshao(self):
        print("本空调是",self.__pinpai,",价格",self.__money)
kongtiao = kongtiao()
kongtiao.setmoney(5000)

kongtiao.setpinpai("海尔")
kongtiao.jieshao()
kongtiao.kaiji()
kongtiao.guanji(60)


#打电话
class phon:
    __name = ""
    __age = None
    __Gender = ""
    __money = None
    __pingpai = ""
    __dianchi = ""
    __chicun = ""
    __daiji = ""
    __jifen = None
    dianhuo = 2

    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age
    def setGender(self,Gender):
        self.__Gender = Gender
    def getGender(self):
        return self.__Gender
    def setmoney(self,money):
        self.__money = money
    def getmoney(self):
        return self.__money
    def setpinpai(self,pinpai):
        self.__pingpai = pinpai
    def getpingpai(self):
        return self.__pingpai
    def setdianchi(self,dianchi):
        self.__dianchi = dianchi
    def getdianchi(self):
        return self.__dianchi
    def setchicun(self,chicun):
        self.__chicun = chicun
    def getchicun(self):
        return self.__chicun
    def setdaiji(self,daiji):
        self.__daiji = daiji
    def getdaiji(self):
        return self.__daiji
    def setjifen(self,jifen):
        self.__jifen = jifen
    def getjifen(self):
        return self.__jifen
    def duanxin(self,neirong):
        print(neirong)
    def dadianhu(self,phone,time):
        if phone == None:
            print("手机号为空！")
            return
        elif self.dianhuo == phone:
            print("不能给自己打电话!")
            return
        else:
            if self.__money < 1:
                print("话费不足！")
                return
            if time > 1 and time <= 10:
                if self.__money < time:
                    print("当前话费余额不能打", time, "分钟的电话！")
                    return
                print("正在给",phone,"打电话。。。")
                self.__money = self.__money - time
                self.__jifen = self.__jifen + time*15
                print("电话已结束，当前话费余额为：￥",round(self.__money,2),",积分为：",self.__jifen)
            elif time > 10 and time <= 20:
                if self.__money < time*0.8:
                    print("当前话费余额不能打", time, "分钟的电话！")
                    return
                print("正在给", phone, "打电话。。。")
                self.__money = self.__money - time*0.8
                self.__jifen = self.__jifen + time * 39
                print("电话已结束，当前话费余额为：￥", round(self.__money,2), ",积分为：", self.__jifen)
            elif time > 20:
                if self.__money < time*0.65:
                    print("当前话费余额不能打", time, "分钟的电话！")
                    return
                print("正在给", phone, "打电话。。。")
                self.__money = self.__money - time*0.65
                self.__jifen = self.__jifen + time * 48
                print("电话已结束，当前话费余额为：￥", round(self.__money,2), ",积分为：", self.__jifen)
            else:
                print("分组输入非法！")
            # elif self.__money < time:
            #     print("当前话费余额不能打",time,"分钟的电话！")

phon = phon()
phon.setpinpai("华为")
phon.setname("张三")
phon.setGender("男")
phon.setage(20)
phon.setmoney(100)#话费
phon.setdianchi("4000ma")
phon.setchicun("6.2寸")
phon.setdaiji("24H")
phon.setjifen(100)#积分
print(phon.getname(),phon.getGender(),phon.getage(),"当前话费余额：￥",phon.getmoney(),phon.getdianchi(),phon.getpingpai(),phon.getdaiji(),phon.getchicun(),"积分：",phon.getjifen())
phon.dadianhu(110,101)



























