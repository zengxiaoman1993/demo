#
import logging
import unittest

from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import read_login_data, assert_common

# 创建unittest的类
class TestIHRMLoginParams(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()

    # 定义登录数据文件的路径
    filepath = app.BASE_DIR + "/data/login_data.json"

    # 编写登录成功函数
    @parameterized.expand(read_login_data(filepath))
    def test01_login(self, case_name, request_body, success, code, message, http_code):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login(request_body,
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为 : {}".format(response.json()))
        assert_common(self, http_code, success, code, message, response)
