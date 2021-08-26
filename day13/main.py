import unittest
from HTMLTestRunner import HTMLTestRunner#测试用例、生成报告
#1.加载所有用例
test = unittest.defaultTestLoader.discover(r"D:\python作业\单元测试",pattern="tset*.py")
#2.用运行器执行这些用例
run = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",#标题
    description="这是加法和减法的测试报告",
    verbosity=1,
    stream=open("计算器报告.html",mode="w+",encoding="utf8")
)
#得到报告
run.run(test)




















