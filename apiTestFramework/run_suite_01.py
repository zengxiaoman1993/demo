
# 1.导包
import os
import time
import unittest
from BeautifulReport import BeautifulReport

# 定位当前项目目录 , 注意 abspath 跟 dirname 的位置 ,  同" HTMLTestRunner_PY3 " 是相反的
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
# 创建测试套件
suite = unittest.TestLoader().discover(BASE_PATH + "/script", "test*.py")
# 定义测试报告名称
report_file = "report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 使用 BeautifulReport 生成测试报告
# with open(report_file, "wb") as f:
BeautifulReport(suite).report(filename=report_file, description="美丽的测试报告", log_path=BASE_PATH + "/report")

