# 生成测试报告时 ,先执行测试用例
# 把测试用例添加到测试套件中, 然后执行测试套件,生成测试报告
# 1.导包
import os
import time
import unittest
import HTMLTestRunner_PY3
from script.test_tpshop_login import TestTpshopLogin

# 定位当前项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 2.创建测试套件
suite = unittest.TestSuite()
# 3.将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestTpshopLogin))
# 4.定义测试报告的目录和报告名称
report_path = BASE_DIR + "/report/tpshop{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 5.使用 HTMLTestRunner_PY3 生成测试报告
with open(report_path, mode="wb") as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="tpshop登录接口功能测试", description="完美的测试报告,前提需联网")
    # 使用实例化的runner运行测试套件
    runner.run(suite)
