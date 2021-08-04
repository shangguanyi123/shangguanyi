'''

input （"提示"）输入

'''
'''name = input ("请输入您的姓名：")
age = input("请输入你的年龄：")
int (age)  #"20" --> 20 把引号去掉
print(name)
print(age)
'''
#起始：5000金币，每猜错一次，减去500金币，金币不够，系统锁定。猜中加10000，问是否进行二轮游戏
import random
user = "admin"
pwd = "123"
print("----------------欢迎来到猜数字游戏----------------")
while True:
    u1 = input("请输入用户名：")
    p1 = input("请输入密码：")
    if u1 == "admin" and p1 == "123":
        print("登录成功!")
        break
    else:
        print("账号或密码错误，请重新输入！")
num = random.randint(0,150)
jinbi = 5000
while jinbi >= 500:
    numb = input("请输入一个数字：")
    numb = int(numb)
    if numb > num:
        print("猜大了")
    elif numb <num:
        print("猜小了")
    else:
        print("恭喜您，猜对了，奖励10000金币，本次数字为：",num,"，当前金币剩余：",jinbi-500+10000)
        #break
        print("是否重新进行游戏，输入1退出游戏，输入其他字符继续游戏：")
        a= input()
        if a == "1" :
            print("游戏结束！")
            break
    jinbi = jinbi - 500
    if jinbi < 500:
        print("金币不足，系统锁定，当前金币余额为：",jinbi)
        break















