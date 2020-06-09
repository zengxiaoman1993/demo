# 导包
import unittest
import logging
from api.login_api import LoginApi
from utils import assert_common


# 创建unittest类
class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写登陆成功函数
    def test01_login_success(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为 : {}".format(response.json()))
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 编写手机号码为空函数
    def test02_mobile_is_empty(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"mobile": "", "password": "error"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号码为空的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 编写手机号码不存在函数
    def test03_mobile_is_not_exists(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"mobile": "13900001122", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号码不存在的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 编写密码错误函数
    def test04_password_is_error(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "error"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("密码错误的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 编写密码为空 的函数
    def test05_password_is_empty(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"moble": "13800000002", "password": ""},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("密码为空 的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 编写无参的函数
    def test06_params_is_none(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("无参的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 编写 null 的函数
    def test07_params_is_null(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login(None,
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info(" Null 的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)

    # 编写多参的函数
    def test08_more_params(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("多参的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 编写少参- 缺少mobile 的函数
    def test09_less_mobile(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("少参- 缺少mobile的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 编写少参- 缺少password 的函数
    def test10_less_password(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"mobile": "13800000002"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("少参- 缺少password的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 编写错误参数 的函数
    def test11_params_is_error(self):
        # 使用封装的接口调用登录接口, 并返回响应数据
        response = self.login_api.login({"moble": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("错误参数 的结果为 : {}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)


