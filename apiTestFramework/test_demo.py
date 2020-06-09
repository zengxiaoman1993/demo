"""
# 导包
import requests

# 需求 : tpshop登录
# 发送获取验证码接口请求
verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
# 实例化 session
session = requests.Session()
session.get(url=verify_url)
# 发送登录接口请求
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
response_login = session.post(url=login_url, data=data)
# 查看结果
print("登录结果为: ", response_login.json())
# 关闭session
session.close()
"""
import requests


class FengzhuangDemo:
    def __init__(self):
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def get_verify(self, session):
        return session.get(url=self.verify_url)

    def login(self, data, session):
        response = session.post(url=self.login_url, data=data)
        return response


session2 = requests.Session()
fengzhuang = FengzhuangDemo()
print(fengzhuang.get_verify(session2).content)
data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
print(fengzhuang.login(data, session2).json())
session2.close()
