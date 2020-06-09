#  导入requests 模块
import requests

# 使用requests 模块发送 get 请求,访问百度首页, 并获取返回的响应数据
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                        json={"mobile": "13800000002", "password": "123456"})
# 打印响应数据
print("ihrm登录的结果为: ", response.json())

