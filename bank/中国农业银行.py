import random
from Bank_Database import Bank_Database#把表Bank_Database里面的Bank_Database类调用过来
#数据库
# bank = [
# {'account': '010', 'name': '3', 'ID': '1', 'password': '1', 'country': '3', 'province': '3', 'street': '3', 'House': '3', 'money': 100000, 'type': '白金卡', 'bankname': '中国农业银行北京昌平支行'},
# {'account': '011', 'name': '3', 'ID': '2', 'password': '1', 'country': '3', 'province': '3', 'street': '3', 'House': '3', 'money': 100000, 'type': '普通卡', 'bankname': '中国农业银行北京昌平支行'},
# {'account': '012', 'name': '3', 'ID': '3', 'password': '1', 'country': '3', 'province': '3', 'street': '3', 'House': '3', 'money': 100000, 'type': '白金卡', 'bankname': '中国农业银行安徽芜湖支行'},
# {'account': '020', 'name': '3', 'ID': '3', 'password': '1', 'country': '3', 'province': '3', 'street': '3', 'House': '3', 'money': 100000, 'type': '白金卡', 'bankname': '中国农业银行安徽芜湖支行'}
#
# ]
#nonghangbank = []
bankuser = Bank_Database#把类Bank_Database的值赋给bankuser 相当于重命名
gonghangbank = bankuser.icbcbank#把类的工商银行用户信息调过来
nonghangbank = bankuser.abcbank#把类的农业银行用户信息调过来

for i in gonghangbank:
    nonghangbank.append(i)#把工商银行的用户信息依次添加到农业银行的用户列表里
# print(len(nonghangbank))
# print(nonghangbank)

bankname = "中国农业银行北京昌平支行"#银行名称


def  getRandom():#随机字符
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string =  string + li[int(random.random()* len(li))]
    return string


#银行开户
def kaihu():
    #数据库大于100时，无法创建新用户
    a = "普通卡"
    b = "白金卡"
    if len(nonghangbank) > 100:
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
        type = input("请选择您办理卡的类型：\n1.普通卡（转出额度每次<=2万）\n2.白金卡（转出额度每次<=5万）\n请输入序号：")
        if type == "1":
            type = a
            #print(a)
        elif type == "2":
            type = b
            #print(b)
        else:
            print("输入错误，请重新输入！")
            return
        account = str(random.randint(10000000,99999999))
        for c in nonghangbank:
            if c["account"] == account:#判断随机分配的账号是否重复
                account = str(random.randint(10000000,99999999))
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
            "type":type,
            "bankname":bankname
        }
        #print("开户成功！请牢记您的卡号：", account)
        #看看账号是否在数据库里
        for i in nonghangbank:
            if i["ID"] == ID:
                print("该证件号的用户已存在，请到其他银行办理！")
                break
        else:
            nonghangbank.append(user)
            print("开户成功！以下是您的个人信息：")
            info = '''
-------------------个人信息------------------
        用户名:%s                                  
        密码：******                               
        账号:%s                                    
        身份证号：%s
        地址：
            省份:%s
            城市:%s
            街道：%s
            门牌号:%s
        余额：%s
        银行卡类型：%s
        开户行:%s
--------------------------------------------
                    '''
            print(info % ( name,account,ID, country, province, street, House, money, type,bankname) )
            #print(bank)

#查询
def chaxun():
    account = input("请输入您要查询的账号：")
    for i in nonghangbank:
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
    for i in nonghangbank:#把银行里的数据依次取出来，赋给i
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
    for i in nonghangbank:#把银行里的数据依次取出来，赋给i
        if i["account"] == account:#如果账号在银行的数据库里
            password = input("请输入取款密码：")
            if i["password"] == password:#判断密码对不对
                money = int(input("请输入取款金额："))

                if int(i["money"]) >= money:
                    i["money"] = int(i["money"]) - money
                    print("取款成功！您的当前余额为：￥",i["money"])
                    return
                elif int(i["money"]) < money:
                    print("余额不足！")
                    break
                else:
                    print("输入错误！请输入数字！！！")
                    break
            else:
                print("密码错误！")
                break
    else:
        print("账号不存在！")





#转账
def zhuangzhang():
    account1 = input("请输入您要转出的账号：")
    for i in nonghangbank:
        if i["account"] == account1:
            password1 = input("请输入密码：")
            if i["password"] == password1:
                account2 = input("请输入您要转入的账号：")
                for j in nonghangbank:
                    if j["account"] == account2:
                        money = input("请输入转账金额：")
                        if int(i["money"]) >= int(money):
                            if i["type"] == "普通卡":
                                if int(money) <= 20000:#普通卡最大转账单次20000元
                                    if j["bankname"] == bankname:
                                        i["money"] = int(i["money"]) - int(money)
                                        j["money"] = int(j["money"]) + int(money)
                                        print("转账成功")
                                        print("转出账户余额：￥", i["money"])
                                        print("转入账户余额：￥", j["money"])
                                        return
                                    elif j["bankname"] == "中国农业银行安徽芜湖支行":
                                        i["money"] = int(i["money"])  - int(money)
                                        j["money"] = int(j["money"])  + int(money)* 0.999
                                        print("转账成功")
                                        print("转出账户余额：￥", i["money"])
                                        print("转入账户余额：￥", j["money"])
                                        return
                                    else:
                                        i["money"] = int(i["money"]) - int(money)
                                        j["money"] = int(j["money"]) + int(money) * 0.998
                                        print("转账成功")
                                        print("转出账户余额：￥", i["money"])
                                        print("转入账户余额：￥", j["money"])
                                        return
                                elif int(money) > 20000:
                                    print("转账失败，请升级为白金卡，每次最大转账额度为5万元！")
                                    return
                            if i["type"] == "白金卡":
                                if int(money) <= 50000:#白金卡单次最大转账50000元
                                    if j["bankname"] == bankname:
                                        i["money"] = int(i["money"]) - int(money)
                                        j["money"] = int(j["money"]) + int(money)
                                        print("转账成功")
                                        print("转出账户余额：￥", i["money"])
                                        print("转入账户余额：￥", j["money"])
                                        return
                                    elif j["bankname"] == "中国农业银行安徽芜湖支行":
                                        i["money"] = int(i["money"]) - int(money)
                                        j["money"] = int(j["money"]) + int(money) * 0.999
                                        print("转账成功")
                                        print("转出账户余额：￥", i["money"])
                                        print("转入账户余额：￥", j["money"])
                                        return
                                    else:
                                        i["money"] = int(i["money"]) - int(money)
                                        j["money"] = int(j["money"]) + int(money) * 0.998
                                        print("转账成功")
                                        print("转出账户余额：￥", i["money"])
                                        print("转入账户余额：￥", j["money"])
                                        return
                                elif int(money) > 50000:
                                    print("尊贵的白金卡用户，单次最大最大转账额度为5万元，请您分次转账！")
                                    return

                        else:
                            print("当前余额不足，请先存款！")
                            break
                else:
                    print("账号不存在！")
                    break
            else:
                print("密码错误！")
                break

    else:
        print("账号不存在！")

#首页面
def welcom():
    print("-------------------------------------------")
    print("-            中国农业银行账户管理系统          -")
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








