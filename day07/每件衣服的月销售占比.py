import xlrd
gzb = xlrd.open_workbook(filename=r"D:\Python自动化测试\python\day07\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
xixi = {}
def yue(i):
#for i in range(0,12):#0~11
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


    sum = 0
    biao = []
    for i in xixi:  # 把每件衣服的销售额放到表里
        # print(xixi[i])
        sum = xixi[i]["单价"] * xixi[i]["销售量"]
        # print(sum)
        biao.append(sum)

    a = 0
    for i in biao:  # 计算销售总额
        a = a + i
    #print(a)
    b = 0
    for i in xixi:  # 输入商品名称
        print(i, "\t", end="")
    print("销售占比分别为：")
    for i in biao:  # 求每件衣服的月销售占比
        b = i / a
        print(round(b * 100, 2), "%\t", end="")
    print()
c = 0
while c < 12:
    print(c + 1, "月",end="")
    yue(c)
    c = c + 1






