import xlrd
gzb = xlrd.open_workbook(filename=r"D:\Python自动化测试\python\day07\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
xixi = {}

for i in range(0,12):#0~11
    biao = gzb.sheet_by_index(i)#打开表
    hang = biao.nrows
    lie = biao.ncols
    for k in range(1,hang):#输出所有行 从角标为1的行开始
        for j in range(lie):#输出所有列
            mingcheng = biao.cell_value(k,1)#输出所有行 角标为1的列
            danjia = biao.cell_value(k,2)#输出所有行 角标为2的列
            jianshu = biao.cell_value(k,4)#输出所有行 角标为4的列
            if mingcheng not in xixi:
                xixi[mingcheng]={
                    "单价":danjia,
                    "销售量":jianshu
                }

            elif mingcheng in xixi:
                xixi[mingcheng] = {
                    "单价": danjia,
                    "销售量": xixi[mingcheng]["销售量"] + jianshu
                }
            break

#每件衣服的销售（件数）占比
zongjian = []#衣服每月总件数表
for i in xixi:#把12个月的销售衣服的总件数放到表里
    #print(xixi[i])
    #print(xixi[i]["销售量"])
    zongjian.append(xixi[i]["销售量"])

sumjian=sum(zongjian)#衣服总件数
#print("总销售量",sums)
a = 0
for j in xixi:
    print(j,"\t",end="")
print("件数占比分别为：")
for i in zongjian:
    a = i / sumjian#求每件衣服的件数总件数的比例
    print(round(a*100,2),"%\t",end="")


#每件衣服的销售额占比
zonge = []
money = 0
for x in xixi:
    money = xixi[x]["单价"] * xixi[x]["销售量"]
    zonge.append(money)
zongmoney= sum(zonge)
#print("总销售额为：",zongmoney)
print()
for i in xixi:
    print(i,"\t",end="")
print("总销售额占比为：")
b = 0
for i in zonge:
    b = i / zongmoney
    print(round(b*100,2),"%\t",end="")

#最畅销的衣服是那种
max = 0
min = 99999
min = max = xixi["羽绒服"]["销售量"]
for j in xixi:
    if max < xixi[j]["销售量"]:
        max = xixi[j]["销售量"]
        a = j
    if min > xixi[j]["销售量"]:
        min = xixi[j]["销售量"]
        b = j
print()
print("销量最好的商品是：",a,max,"件，销量最差的商品是：",b,min,"件！")















