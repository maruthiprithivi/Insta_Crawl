__author__ = 'Maruthi'

import json
import yaml
import ast
import pickle

tokenD = open("token.json")
# with open('token.json')as tokenD:
# for item in tokenD:
    # x = item['token1']
    # print x
    # print type(item)
data = json.load(tokenD)
# data1 = pickle.load(tokenD)
# data1 = ast.literal_eval(tokenD)
# data = [s.encode('utf-8') for s in data]
# data1 = yaml.safe_load(tokenD)
print data
# print data1
# print data1
tk1 = data["token1"]
# data = [s.encode('utf-8') for s in tk1]
tk2 = data["token2"]
# data = [s.encode('utf-8') for s in tk2]
print tk1
print tk2

# print data
# print data1