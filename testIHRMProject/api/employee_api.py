# 导包
import requests


# 创建封装的员工类
class EmployeeApi:
    def __init__(self):
        # 定义员工模块的url
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"

    def add_emp(self, username, mobile, headers):
        # 根据外部传入的username和mobile拼接成要发送的请求体数据
        jsonData = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": "2020-05-05",
                    "formOfEmployment": 1,
                    "departmentName": "测试部",
                    "departmentId": "1063678149528784896",
                    "correctionTime": "2020-05-30T16:00:00.000Z"
                    }
        # 发送员工请求, 并返回结果
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    def query_emp(self, emp_id, headers):
        # 拼接查询员工接口的 url
        query_url = self.emp_url + "/" + emp_id
        # 发送查询员工接口的请求 ,并返回结果
        return requests.get(url=query_url, headers=headers)

    def modify_emp(self, emp_id, jsonData, headers):
        # 拼接修改员工接口的 url
        modify_url = self.emp_url + "/" + emp_id
        # 发送修改员工接口的请求, 并返回数据
        return requests.put(url=modify_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):
        # 拼接删除员工接口的 url
        delete_url = self.emp_url + "/" + emp_id
        # 发送删除员工接口的请求, 并返回数据
        return requests.delete(url=delete_url, headers=headers)




