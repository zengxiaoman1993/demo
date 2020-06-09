# 导入requests
import requests

# 发送登录的接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 打印登录的结果
print("登录的结果为: ", response.json())
# 提取登录返回的令牌
token = 'Bearer ' + response.json().get('data')
print("提取的令牌为: ", token)

# 发送添加员工接口
headers = {"Content-Type": "application/json", "Authorization": token}
response = requests.post(url="http://ihrm-test.itheima.net" + "/api/sys/user",
                         json={"username": "皮卡丘与可达鸭呀呀004",
                               "mobile": "15978891063",
                               "timeOfEntry": "2020-05-05",
                               "formOfEmployment": 1,
                               "departmentName": "测试部",
                               "departmentId": "1063678149528784896",
                               "correctionTime": "2020-05-30T16:00:00.000Z"
                               },
                         headers=headers)
# 打印添加员工的接口
print("添加员工的接口返回数据为: ", response.json())
# 提取添加员工接口返回的员工 id
emp_id = response.json().get('data').get('id')
print("提取的员工 id 为: ", emp_id)

# 拼接查询员工接口的 url
query_url = "http://ihrm-test.itheima.net" + "/api/sys/user"+"/"+emp_id
print("查询员工接口的 URL : ", query_url)
# 发送查询员工接口的请求
response = requests.get(query_url, headers=headers)
# 打印查询员工的结果
print("打印查询员工的结果为: ", response.json())

# 拼接修改员工接口的 url
modify_url = "http://ihrm-test.itheima.net" + "/api/sys/user"+"/"+emp_id
# 发送修改员工接口的请求
response = requests.put(url=modify_url, json={"username": "可爱的皮卡丘会发电"}, headers=headers)
# 打印修改员工的结果
print("被修改员工的结果为: ", response.json())

# 拼接删除员工接口的 url
delete_url = "http://ihrm-test.itheima.net" + "/api/sys/user"+"/"+emp_id
# 发送删除员工接口的请求
response = requests.delete(url=delete_url, headers=headers)
# 打印删除员工的结果
print("删除员工的结果为: ", response.json())
