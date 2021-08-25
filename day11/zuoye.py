class chushi:
    __name = ""
    __age = 0
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age

class chuzi(chushi):
    chaocai = ""
    def chaoc(self):
        print("厨师正在做",self.chaocai)

class tudi(chuzi):
    zuofan = ""
    def zuof(self):
        print("徒弟正在做",self.zuofan)




t = tudi()
t.setname("张三")
t.setage(10)
print(t.getname(),t.getage())


t.zuofan = "老干妈炒饭"
t.chaocai = "酸菜鱼"
print(t.chaoc(),t.zuof())
























