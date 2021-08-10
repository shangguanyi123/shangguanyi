import random
#数据库
bank = [
{'account': '111', 'name': '1', 'ID': '1', 'password': '1', 'country': '1', 'province': '1', 'street': '1', 'House': '1', 'money': '100', 'bankname': '中国银行昌平支行'},
{'account': '222', 'name': '2', 'ID': '2', 'password': '2', 'country': '2', 'province': '2', 'street': '2', 'House': '2', 'money': '100', 'bankname': '中国银行昌平支行'}
]
bankname = "中国银行昌平支行"#银行名称


def  getRandom():#随机字符
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string =  string + li[int(random.random()* len(li))]
    return string


#银行开户
def kaihu():
    #数据库大于100时，无法创建新用户
    if len(bank) > 100:
        print("当前数据库已满，请联系工作人员！")
    else:
        name = input("请输入您的姓名：")
        ID = input("请输入您的身份证号码：")
        password = input("请设置您的密码：")
        country = input("请输入您所在的省份：")
        province = input("请输入你所在的城市：")
        street = input("请输入您所在的街道：")
        House = input("请输入您的门牌号：")
        money = int(input("请输入您的预存款："))
        account = getRandom()
        user = {
            "account":account,
            "name":name,
            "ID": ID,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "House":House,
            "money":money,
            "bankname":bankname
        }
        #print("开户成功！请牢记您的卡号：", account)
        #看看账号是否在数据库里
        for i in bank:
            if i["ID"] == ID:
                print("该证件号的用户已存在，请到其他银行办理！")
                break
        else:
            bank.append(user)
            print("开户成功！请牢记您的卡号：",account)
            #print(bank)

#查询
def chaxun():
    account = input("请输入您要查询的账号：")
    for i in bank:
        if i["account"] == account:
            password = input("请输入密码：")
            if i["password"] == password:
                print(i)
                break
            else:
                print("密码错误!!!")
                break
    else:
        print("账号不存在！！！")



#存钱
def cunqian():
    account = input("请输入您要存入的账号：")
    for i in bank:#把银行里的数据依次取出来，赋给i
        if i["account"] == account:#如果账号在银行的数据库里
            money = input("请输入存款金额：")
            i["money"] = int(i["money"])+int(money)
            print("您的当前余额为：￥",i["money"])
            break
    else:
        print("账号不存在！！！")


#取钱
def qvqian():
    account = input("请输入您要取款的账号：")
    for i in bank:#把银行里的数据依次取出来，赋给i
        if i["account"] == account:#如果账号在银行的数据库里
            password = input("请输入取款密码：")
            if i["password"] == password:#判断密码对不对
                money = int(input("请输入取款金额："))

                if int(i["money"]) >= money:
                    i["money"] = int(i["money"]) - money
                    print("取款成功！您的当前余额为：￥",i["money"])
                    break
            else:
                print("密码错误！")
                break
    else:
        print("账号不存在！")


#转账
def zhuangzhang():
    account1 = input("请输入您要转出的账号：")
    for i in bank:
        if i["account"] == account1:
            password1 = input("请输入密码：")
            if i["password"] == password1:
                account2 = input("请输入您要转入的账号：")
                for j in bank:
                    if j["account"] == account2:
                        money = input("请输入转账金额：")
                        if int(i["money"]) >= int(money):
                            i["money"] = int(i["money"]) - int(money)
                            j["money"] = int(j["money"]) + int(money)
                            print("转账成功！")
                            print("转出账户余额：￥",i["money"])
                            print("转入账户余额：￥",j["money"])
                            return
                        else:
                            print("当前余额不足，请先存款！")
                            break
                else:
                    print("账号不存在！")

            else:
                print("密码错误！")
                break
    else:
        print("账号不存在！")









#首页面
def welcom():
    print("-------------------------------------------")
    print("-              中国银行账户管理系统           -")
    print("-------------------------------------------")
    print("- 1.开户                                   -")
    print("- 2.存钱                                   -")
    print("- 3.取钱                                   -")
    print("- 4.转账                                   -")
    print("- 5.查询                                   -")
    print("- 6.Bys!                                  -")
    print("-------------------------------------------")

while True:
    welcom()#打印首页面
    bianhao = input("请输入您要办理的业务编号：")
    if bianhao == "1":
        kaihu()
    elif bianhao == "2":
        cunqian()
    elif bianhao == "3":
        qvqian()
    elif bianhao == "4":
        zhuangzhang()
    elif bianhao == "5":
        chaxun()
    elif bianhao == "6":
        print("欢迎下次使用！")
        break
    else:
        print("输入有误，请重新输入！")










