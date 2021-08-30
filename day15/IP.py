biao = open(file=r"D:\Python自动化测试\python\python\day15【异常和文件读取和写入】\任务\baidu_x_system.log",mode="r+",encoding="utf-8")
hang = biao.readline()#以行的形式读取文件
li = []
while hang:
    a = hang.split()
    b = a[0]#读取第一行数据
    li.append(b)
    hang = biao.readline()
biao.close()#关闭资源
for index,value in enumerate(li):
    if value in li[:index]:#切片 如果value在从零角标开始到现在这个值-1出现过，直接跳过这一轮
        continue
    print(value,"出现了",li.count(value),"次！")























