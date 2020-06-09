#  导入requests 模块
import requests
# 使用requests 模块发送 get 请求,访问百度首页, 并获取返回的响应数据
response = requests.get(url="http://www.baidu.com")
# 打印响应数据
print("响应结果为: ", response.text)


