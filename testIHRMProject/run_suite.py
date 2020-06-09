
# 1.导包
import time
import unittest
from BeautifulReport import BeautifulReport
from app import BASE_DIR

# 创建测试套件
suite = unittest.TestLoader().discover(BASE_DIR + "/script", "test*params.py")
# 定义测试报告名称
report_file = "report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 使用 BeautifulReport 生成测试报告
# with open(report_file, "wb") as f:
BeautifulReport(suite).report(filename=report_file, description="员工模块增删改查测试", log_path=BASE_DIR + "/report")

