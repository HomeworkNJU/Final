# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:35:54 2018

@author: xiaoyang
"""

N = int(input())
s=input().split(' ')
a=[]
for i in range(N):
    a.append(int(s[i]))
#老方法,相当于直接分配
oldlist = [[],[],[]]
for i in range(N):
    oldlist[i%3].append(a[i])
oldtime = 0
for j in range(3):
    time1 = 0
    for time in oldlist[j]:
        time1 += time
        oldtime += time1
finishold = max([sum(oldlist[0]),sum(oldlist[1]),sum(oldlist[2])])

#新方法
newlist=[0,0,0]
newtime = 0
for time in a:
    for j in range(3):
        if newlist[j]==0:
            newlist[j]=time
    ope_time = min(newlist)
    newtime += ope_time
    for j in range(3):
        newlist[j] -= ope_time
finishnew= newtime + max(newlist)
print(oldtime,finishold)
print(newtime,finishnew)
