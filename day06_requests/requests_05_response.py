# 导入 requests
import requests
# 1. 访问百度首页的接口, 获取响应数据
response = requests.get(url="http://www.baidu.com")
# 2. 获取响应码
print("获取响应码: ", response.status_code)
# 3. 获取请求 URL
print("获取请求 URL: ", response.url)
# 4. 获取响应码字符编码
print("获取响应码字符编码: ", response.encoding)
# 5. 获取响应头数据
print("获取响应头数据: ", response.headers)
# 6. 获取响应码的cookie数据
print("获取响应码的cookie数据: ", response.cookies)
# 7. 获取文本形式的响应数据
# print("获取文本形式的响应数据: ", response.text)
# 8. 获取字节形式的响应内容
print("获取字节形式的响应内容: ", response.content)


