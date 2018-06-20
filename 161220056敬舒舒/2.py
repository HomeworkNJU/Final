# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:17:28 2018

@author: Alice_shu
"""

nums = int(input("请输入进入人数："))
time = input("请输入每个人占用柜台时间（空格分开）：").split()
for i in range(nums):
    time[i] = int(time[i])
#传统方法
#三个队列和对应人数
List= [[],[],[]]
L = [0,0,0]
T = [0,0,0]
W1 = 0
T1 = 0
for i in range(nums):
    x = min(L)
    for j in range(3):
        if L[j] == x:
            List[j].append(time[i])
            L[j] += 1
            break
for i in range(3):
    x = len(List[i])
    for j in range(x-1):
        T[i] += List[i][j]
    for j in range(x):
        for k in range(j):
            W1 += List[i][k]
    T[i] += List[i][x-1]
T1 = max(T)
print("旧方法总等待时间：%d\n旧方法处理完成时刻：%d" % (W1,T1))
#新方式
NList = [0,0,0]
W2 = 0
T2 = 0
Ti = -1
peo = 0
while peo != nums:
    for i in range(3):
        if NList[i] == 0:
            NList[i] = time[peo]
            peo += 1
            if peo == nums:
                break
        NList[i] -=1
    W2 = W2 + nums - peo
    Ti += 1
T2 = Ti + max(NList) - 1
print("新方法总等待时间：%d\n新方法处理完成时刻：%d" % (W2,T2))

            