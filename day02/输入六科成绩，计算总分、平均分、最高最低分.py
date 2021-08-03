num = []
cishu = 1
while cishu <=6:
    print("请输入第",cishu,"课的成绩：")
    shu = int(input())
    num.append(shu)
    shu = int(shu)
    cishu = cishu + 1
    #print(num)
print("最大值为：", max(num))
print("最小值：",min(num) )
print("平均值为：",sum(num)/6)
print("z总和为：",sum(num))