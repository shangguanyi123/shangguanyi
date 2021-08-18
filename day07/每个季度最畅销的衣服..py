import xlrd
gzb = xlrd.open_workbook(filename=r"D:\Python自动化测试\python\day07\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
xixi = {}

def ji(i):#0~11
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
def xiaoliang():
    min = max = xixi["羽绒服"]["销售量"]
    for j in xixi:
        if max < xixi[j]["销售量"]:
            max = xixi[j]["销售量"]
            a = j
        if min > xixi[j]["销售量"]:
            min = xixi[j]["销售量"]
            b = j

    print("销量最好的商品是：",a,max,"件，销量最差的商品是：",b,min,"件！")
ji(1)
ji(2)
ji(3)
print("一季度",end="")
xiaoliang()
ji(4)
ji(5)
ji(6)
print("二季度",end="")
xiaoliang()
ji(7)
ji(8)
ji(9)
print("三季度",end="")
xiaoliang()
ji(10)
ji(11)
ji(0)
print("四季度",end="")
xiaoliang()