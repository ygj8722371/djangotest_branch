# import requests
# import json
# import requests
# import json
# proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
# url = 'http://www.baidu.com'
# data = {"username":"admin"}
# requests.post(url, proxies=proxies, verify=False,data=json.dumps(data))
# requests.post(url, proxies=proxies, verify=False,data=data)

# import requests
# import json
# payload = {"key1": "value1", "key2": "value2"}
# r = requests.post("http://httpbin.org/post", data=payload)
# r = requests.post("http://httpbin.org/post", data=json.dumps(payload))
# r = requests.post("http://httpbin.org/post", json=payload)
# print(r.text)


# def tj(list):
#     dict1 = {}
#     for i in list:
#         if i not in dict1:
#             dict1[i] = 1
#         else:
#             dict1[i]+=1
#     return dict1
# list1 = [1,2,3,4,5,3,2,1]
# print(tj(list1))

# a = 'a'
# print(dir(a))
# print(dict(a))