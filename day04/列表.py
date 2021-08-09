'''
    数据类型：
        int
        str:
        bool
        float,double

        容器类型：
            元组：(1,2,3,4,5,6)
                不能做任何修改操作
            列表：[1,12,3,4,4,81,5,10]
                增，删，改，查
            字典：{
                key:value,
                key1:value1
            }
            集合：sets() 不能存储重复元
'''
# li = [15,6,8,7,10]
#
# # 增
# li.append(25)
#
# # 删除
# # del li[0]
#
# # 修改
# li[0] = 30
#
# # 单个查询  ： 列表名称[角标]
# print(li[0])
# print(li[1])


# 随机点名程序
'''
        随机点名
    需求：
        系统随机从列表中抽取一名幸运观众。
    技术选型：
        random
        列表取数据
'''
import random
names = ["张三","李四","王五","赵六","旺财","jason"]
index = random.randint(0,5)
print(names[index])



for key,value in enumerate(names):
    print(key,value) # 0 张三       1  李四

