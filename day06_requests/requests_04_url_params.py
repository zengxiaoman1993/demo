#  导入requests 模块
import requests

# 使用requests 模块发送 get 请求, 并获取返回的响应数据
# 访问百度搜索接口
response = requests.get(url="http://www.baidu.com/S", params={"wd": "齐天大圣"})
# 打印响应数据
print("返回的结果为: ", response.text)



