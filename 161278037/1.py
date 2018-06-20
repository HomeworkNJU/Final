# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:10:43 2018

@author: xiaoyang
"""

s = input().split(' ')
s[0] = int(s[0])
s[1] = int(s[1])
print("%10d"%(s[0]))
print("%10d"%(s[1]))
print('        --')
result = s[0]*s[1]
resultlist = []
strsep = ''
while True:
    if s[1]>0:
        resultlist.append(str(s[1]%10*s[0])+strsep)
        s[1] = s[1]//10
        strsep += ' '
    else:
        break
for i in resultlist:
    print("%10s"%(i))
if len(resultlist)>1:    
    print('        --')
    print('%10d'%result)
