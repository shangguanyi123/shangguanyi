'''
    1.准备数据
    2.执行用例
    3.对别结果，分析结果，得出报告

    2.1导入本身再带测试工具：unittest
    2.2测试用例类继承unittest.TsetCase
    2.3写测试用例
        注意：用例的方法必须是tsetxxxx开头
    3.生成一份测试报告()
        生成一个html的测试报告
'''
#from Calc import jisuanqi
# #1.准备数据
# a = 5
# b = 10
# c = 15
# #2.执行用例
# calc = jisuanqi()
# s = calc.add(a,b)
# #3.对比期望结果和实际结果
# if s == c :
#     print("用例通过！")
# else:
#     print("用例不通过！")
from Calc import jisuanqi
import unittest#导入测试工具
class Tsetjisuanqi(unittest.TestCase):#继承unittest.TsetCase
    def testadd1(self):
        #1.准备数据
        a = 5
        b = 10
        c = -5
        #2.执行用例
        calc = jisuanqi()
        s = calc.jian(a,b)
        #3.断言期望结果
        self.assertEqual(c,s)
    def testadd2(self):
        #1.准备数据
        a = -5
        b = -10
        c = 5
        #2.执行用例
        calc = jisuanqi()
        s = calc.jian(a,b)
        #3.断言期望结果
        self.assertEqual(c,s)
    def testadd3(self):
        #1.准备数据
        a = -5
        b = 10
        c = -15
        #2.执行用例
        calc = jisuanqi()
        s = calc.jian(a,b)
        #3.断言期望结果
        self.assertEqual(c,s)
    def testadd4(self):
        #1.准备数据
        a = 5
        b = -10
        c = 15
        #2.执行用例
        calc = jisuanqi()
        s = calc.jian(a,b)
        #3.断言期望结果
        self.assertEqual(c,s)
    def testadd5(self):
        #1.准备数据
        a = -1000000000000000000000000000000000
        b = -1000000000000000000000000000000000
        c = 0
        #2.执行用例
        calc = jisuanqi()
        s = calc.jian(a,b)
        #3.断言期望结果
        self.assertEqual(c,s)
    def testadd6(self):
        #1.准备数据
        a = 1000000000000000000000000000000000
        b = 1000000000000000000000000000000000
        c = 0
        #2.执行用例
        calc = jisuanqi()
        s = calc.jian(a,b)
        #3.断言期望结果
        self.assertEqual(c,s)


















