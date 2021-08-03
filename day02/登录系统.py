a = 1
user = 'root'
pwd = 'admin'
while a <=3:
    u1 = input("请输入用户名：")
    p1 = input("请输入密码：")
    if u1 == user and p1 == pwd:
        print("登陆成功！")
        break
    else:
        print("用户名或密码错误！")
    a = a + 1
else:
    print("三次账号或密码输入错误，系统锁定！")