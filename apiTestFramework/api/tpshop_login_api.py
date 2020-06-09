# 导包

# 定义封装的类
class TestTpshopApi:
    # 初始化 验证码 URL 和登录URL
    def __init__(self):
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 封装获取验证码
    def get_verify(self, session):
        # 发送获取验证码请求并直接 return返回的对象
        return session.get(url=self.verify_url)

    # 封装登录接口
    def login(self, data, session):
        # 发送登录接口请求 ,并直接return
        return session.post(url=self.login_url, data=data)
