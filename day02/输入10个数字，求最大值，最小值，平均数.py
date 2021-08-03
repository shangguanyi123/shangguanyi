'''
方案一：
cishu = 1
sum = 0
max = 0
while cishu <= 3:
    print("请输入第",cishu,"个数")
    shu = input()
    shu = int(shu)
    if shu > max:
        max = shu
    sum = sum + shu
    cishu = cishu +1
print("最大值为：",max)
print("总和为：",sum)
print("平均值为：",sum/10)
'''

num = []
cishu = 1
while cishu <=10:
    print("请输入第",cishu,"个数：")
    shu = int(input())
    num.append(shu)
    shu = int(shu)
    cishu = cishu + 1
    print(num)
print("最大值为：", max(num))
print("平均值为：",sum(num)/10)
print("总和为：",sum(num))
