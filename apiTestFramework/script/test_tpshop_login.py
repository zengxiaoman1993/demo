# 导包
import requests
import unittest

# 创建测试函数继承 unittest.TestCase
from api.tpshop_login_api import TestTpshopApi


class TestTpshopLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化封装的登录接口类
        cls.login_api = TestTpshopApi()
        # 实例化session
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()

    def test01_login_success(self):
        """
        登录成功的测试

        """
        # 发送获取验证码的请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data ={"username": "13800138006","password": "123456","verify_code": "8888"}
        response = self.login_api.login(data,self.session)
        # 打印登录结果
        print("登录的结果为: ", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))

    def test02_username_is_not_exist(self):
        """
        用户名不存在的测试

        """
        # 发送获取验证码的请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800138888", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 打印登录结果
        print("登录的结果为: ", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

    def test03_password_error(self):
        """
        密码错误的测试

        """
        # 发送获取验证码的请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800138006", "password": "12345678", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 打印登录结果
        print("登录的结果为: ", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))