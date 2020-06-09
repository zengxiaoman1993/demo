
"""
1.请使用python的requests模块编写对百度进行搜索的代码，搜索关键字：接口测试，接口信息如下：
域名：www.baidu.com 协议：http 请求路径：/s 请求方式：Get 请求参数：wd=xxx

"""
# 导包
import requests
# 访问百度搜索接口, 搜索关键字：接口测试
response = requests.get(url="http://www.baidu.com/S", params={"wd": "接口测试"})
# 打印响应数据
print("返回的搜索文本为 :", response.text)

