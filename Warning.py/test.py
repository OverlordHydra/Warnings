import json, os, re
for i in range(10):
    print(' ')



object_open_dict = {'name':1}
object_open_dict['Guild'] = {"warn": 0}
js = json.dumps(object_open_dict, indent=4)
print(js)



js = json.loads(js)
jv = json.dumps(js)
print("-------------------")
print(jv)
for i in range(5):
    print(' ')
js = js["Guild"]
print(js["warn"])

path_current = os.getcwd()+"/warnings"
path_result = os.path.exists(path_current)



aa = {"id": 12033845953, "total_warn": 10, 3434598648: {"warn": 1, 1 : "Faild to listen to staff"}}
aa = json.dumps(aa, indent=5)

print(aa)
aa = json.load(aa)

aa["chic"] = 'ht'
print(aa)