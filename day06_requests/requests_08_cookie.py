# #  导入requests 模块
# import requests
# # 获取验证码
# response_verify = requests.post(url="http://127.0.0.1/index.php?m=Home&c=User&a=verify")
# # 获取验证码接口返回的 cookie
# cookie = response_verify.cookies
# print("获取的 cookie 为: ", cookie)
# # 登录
# response_login = requests.post(url="http://127.0.0.1/index.php?m=Home&c=User&a=do_login",
#                                data={"username": "2921097111@qq.com", "password": "123456", "verify_code": "8888"},
#                                cookies=cookie)
# print("登录的结果为: ", response_login.json())
# # 访问我的订单
# response_order = requests.get(url="http://127.0.0.1/index.php/Home/Order/order_list.html",
#                               cookies=cookie)
# print("我的订单结果为: ", response_order.text)




