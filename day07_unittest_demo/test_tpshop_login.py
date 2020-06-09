# 导入 unittest 和 requests 模块
import unittest
import requests


# 创建集成 unittest.TestCase 的测试类
class TestTpshopLogin(unittest.TestCase):
    # 编写 unittest.TestCase 类中支持的初始化函数
    def setUp(self):
        # 定义获取验证码和登录的 URL
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        pass    # 不能在此关闭, 已在类中关闭

    # 实例化当前类(unittest.TestCase)时, 运行的函数
    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()

    # 类结束后, 运行的函数, 关闭释放资源
    @classmethod
    def tearDownClass(cls):
        # 关闭 session
        if cls.session != None:
            cls.session.close()

    # 编写测试函数
    # 登录成功
    def test01_login_success(self):
        # 使用实例化 session 调用获取验证码接口
        response_verify = self.session.get(url=self.verify_url)
        # 断言验证码接口返回的响应数据当中的响应头 Content-Type的值是不是一个图片
        # print("打印图片内容: ", response_verify.content)
        # print("返回的响应头: ", response_verify.headers)
        self.assertIn("image", response_verify.headers.get("Content-Type"))

        # 继续使用实例化的 session 调用登录接口
        response_login = self.session.post(url=self.login, data={"username": "13800138006",
                                                                 "password": "123456",
                                                                 "verify_code": "8888"})
        # 打印登录的结果
        print("登录的结果为: ", response_login.json())
        # 根据用例断言登录的结果
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(1, response_login.json().get("status"))
        self.assertIn("登陆成功", response_login.json().get("msg"))

    # 账号不存在
    def test02_username_is_not_exit(self):
        # 使用实例化 session 调用获取验证码接口
        response_verify = self.session.get(url=self.verify_url)
        # 断言验证码接口返回的响应数据当中的响应头 Content-Type的值是不是一个图片
        # print("打印图片内容: ", response_verify.content)
        # print("返回的响应头: ", response_verify.headers)
        self.assertIn("image", response_verify.headers.get("Content-Type"))

        # 继续使用实例化的 session 调用登录接口
        response_login = self.session.post(url=self.login, data={"username": "13800138888",
                                                                 "password": "123456",
                                                                 "verify_code": "8888"})
        # 打印登录的结果
        print("登录的结果为: ", response_login.json())
        # 根据用例断言登录的结果
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(-1, response_login.json().get("status"))
        self.assertIn("账号不存在", response_login.json().get("msg"))

    # 密码错误
    def test03_password_error(self):
        # 使用实例化 session 调用获取验证码接口
        response_verify = self.session.get(url=self.verify_url)
        # 断言验证码接口返回的响应数据当中的响应头 Content-Type的值是不是一个图片
        # print("打印图片内容: ", response_verify.content)
        # print("返回的响应头: ", response_verify.headers)
        self.assertIn("image", response_verify.headers.get("Content-Type"))

        # 继续使用实例化的 session 调用登录接口
        response_login = self.session.post(url=self.login, data={"username": "13800138006",
                                                                 "password": "12345678",
                                                                 "verify_code": "8888"})
        # 打印登录的结果
        print("登录的结果为: ", response_login.json())
        # 根据用例断言登录的结果
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(-2, response_login.json().get("status"))
        self.assertIn("密码错误", response_login.json().get("msg"))
