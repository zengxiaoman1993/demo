import requests
response = requests.get(url="http://www.weather.com.cn/data/sk/101010100.html")
print("获取的天气信息为: ", response.json())
print()
print("获取字节码信息: ", response.content.decode('utf-8'))


