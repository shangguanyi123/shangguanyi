import xlrd
#打开工作铺
gzb = xlrd.open_workbook(filename=r"D:\Python自动化测试\python\day07\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
#打开表
biao = []
def xiaoshoue(a):
    biao1 = gzb.sheet_by_index(a)#打开表
    #单价
    money = biao1.col_values(2)#输出角标为2的列
    #件数
    jian = biao1.col_values(4)#输出角标为2的列
    danjia = []
    jiage = []
    for i in money[1:]:#把单价列 从角标1开始取到结束 并存放在单价表里
        danjia.append(i)
    for j in jian[1:]:
        jiage.append(j)
    a = [a*b for a,b in zip(danjia,jiage)]#价格*单价 列表相乘
    #print(a)
    sum = 0
    for i in a:
        sum += i
    biao.append(sum)
    #print(biao)
    #print(sum)


a = 0
while a <12:
    xiaoshoue(a)
    a +=1
sum = 0
for i in biao:
    sum += i
    #print(sum)
print("全年销售总额为：￥",'%.2f' % sum)





