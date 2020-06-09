#  导入requests 模块
import requests

# 使用requests 模块发送 get 请求,访问登录页面, 并获取返回的响应数据
response = requests.post(url="http://127.0.0.1/index.php/Home/user/login.html",
                        data={"username": "2921097111@qq.com", "password": "123456", "verify_code": "8888"})
# 打印响应数据
print("tpshop登录的结果为: ", response.text)



