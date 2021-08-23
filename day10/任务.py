
#高度，容积，颜色，材质
#能存放液体
class shuibei:
    __gaodu = ""
    __rongji = ""
    __yanse = ""
    __caizhi = ""
    __yeti = ""
    def setgaodu(self,gaodu):
        self.__gaodu = gaodu
    def getgaodu(self):
        return self.__gaodu
    def setrongji(self,rongji):
        self.__rongji=rongji
    def getrongji(self):
        return self.__rongji
    def setyanse(self,yanse):
        self.__yanse = yanse
    def getyanse(self):
        return self.__yanse
    def setcaizhi(self,caizhi):
        self.__caizhi = caizhi
    def getcaizhi(self):
        return self.__caizhi
    def setyeti(self,yeti):
        self.__yeti = yeti
    def getyeti(self):
        return self.__yeti
shuibei = shuibei()
shuibei.setgaodu("20cm的杯子")
shuibei.setrongji("2升")
shuibei.setyanse("白色")
shuibei.setcaizhi("塑料")
shuibei.setyeti("黑色的饮料")
print("有一个",shuibei.getyanse(),shuibei.getcaizhi(),shuibei.getgaodu(),",里面装着",shuibei.getyeti(),",大约有",shuibei.getrongji())

#有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class diannao:
    __chicun = ""
    __money = 0
    __cpu = ""
    __neicun = ""
    __daiji = ""
    __dazi = ""
    __youxi = ""
    __shipin = ""
    def setchicun(self,chicun):
        self.__chicun = chicun
    def getchicun(self):
        return self.__chicun
    def setmoney(self,money):
        if money <= 0:
            print("价格错误！！！")
        elif money > 0:
            self.__money = money
        else:
            print("输入非法！")
    def getmoney(self):
        return self.__money
    def setcpu(self,cpu):
        self.__cpu = cpu
    def getcpu(self):
        return self.__cpu
    def setneicun(self,neicun):
        self.__neicun = neicun
    def getneicun(self):
        return self.__neicun
    def setdaiji(self,daiji):
        self.__daiji = daiji
    def getdaiji(self):
        return self.__daiji
    def setdazi(self, dazi):
        self.__dazi = dazi
    def getdazi(self):
        return self.__dazi
    def setyouxi(self, youxi):
        self.__youxi = youxi
    def getyouxi(self):
        return self.__youxi
    def setshipin(self, shipin):
        self.__shipin = shipin
    def getshipin(self):
        return self.__shipin
    def zong(self):
        print("我买了一个",self.__chicun,"的电脑，cpu是",self.__cpu,"，内存是",self.__neicun,"可以待机",self.__daiji)
        print("可以用它来看",self.__shipin,",玩",self.__youxi,",还可以用它来练习",self.__dazi)
diannao = diannao()
diannao.setchicun("28寸")
diannao.setcpu("i9")
diannao.setneicun("16G")
diannao.setmoney(10000)
diannao.setdaiji("10h")
diannao.setshipin("视频")
diannao.setyouxi("游戏")
diannao.setdazi("打字")
diannao.zong()















