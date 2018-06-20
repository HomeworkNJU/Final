# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:05:04 2018

@author: Alice_shu
"""
#计算佣金 x交易额
def cost(x):
    y = x * 0.002
    if y < 5:
        y = 5
    return y

action = []
record = []
money = 0
action_num = int(input("请输入交易动作数量："))
for i in range(action_num):    
    action.append(input().split())
    for j in range(3):
        action[i][j] = int(action[i][j])
record_num = int(input("请输入股票记录数量："))
for i in range(record_num):    
    record.append(input().split())
    for j in range(2):
        record[i][j] = int(record[i][j])
for i in range(action_num):
    for j in range(record_num - 1):
        if  action[i][0] >= record[record_num-1][0]:
            a = action[i][1] * record[record_num-1][1] * 100
            fee = cost(a) + action[i][1] / 10 + 1
            if action[i][2] == 1:
                money = money - a - fee
            else:
                money = money + a -fee - a * 0.001
        elif action[i][0] < record[j+1][0] and action[i][0] >= record[j][0]:
            a = action[i][1] * record[j][1] * 100
            fee = cost(a) + action[i][1] / 10 + 1
            if action[i][2] == 1:
                money = money - a - fee
            else:
                money = money + a -fee - a * 0.001
print("小明的现金收益为：%.2f" % money)
                
                

