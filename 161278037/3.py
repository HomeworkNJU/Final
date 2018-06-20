# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:41:31 2018

@author: xiaoyang
"""

m = int(input())
a = []
for i in range(m):
    temp = input().split(' ')
    a.append(temp)
n = int(input())
b = []
for i in range(n):
    temp = input().split(' ')
    b.append(temp)
exchange = []
for i in a:
    time = int(i[0])
    for j in b:
        if time <= int(j[0]):
            exchange.append([int(j[1]),int(i[1])*100,int(i[2])])
            break
zhichu = 0
shouru = 0
cje = 0
for i in exchange:
    cje = i[0]*i[1]
    if i[2] == 2:
        zhichu += cje*0.001
        shouru += cje
    else:
        shouru -= cje
    zhichu += max([cje*0.002,5])+i[1]*0.001 + 1
   
print("%.2f"%(shouru - zhichu))
    
