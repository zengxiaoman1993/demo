#  导入requests 模块
import requests

# 需求: 访问 IHRM 的登录接口, 但是要求设置请求头
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                        json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type":"application/json"})
# 打印响应数据
print("设置请求头之后的结果为: ", response.json())