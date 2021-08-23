class student:
    __name = ""
    __age = None
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age
    def zwjs(self):
        print("大家好，我叫",self.__name,",今年",self.__age,"岁了！")
    def compare(self,student):
        if self.__age > student.getage():
            print("我比同桌大",(self.__age - student.getage()),"岁！")
        elif self.__age <student.getage():
            print("我比同桌小", (student.getage() - self.__age), "岁！")
        else:
            print("我俩一样大！")


student1 = student()
student1.setage(25)
student1.setname("张三")
student1.zwjs()
student2 = student()
student2.setname("李四")
student2.setage(20)
student1.compare(student2)
#student2.compare(student1)

























