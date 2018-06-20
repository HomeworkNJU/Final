# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:38:58 2018

@author: Alice_shu
"""

N,P = input().split()
N = int(N)
P = int(P)
loc = []
loc = input().split()
for i in range(N):
    loc[i] = int(loc[i])
P_loc = loc[0:P]
for i in range(P):
    for j in range(i,P):
        for k in range(j,P):
            for m in range(k,P):
                for n in range(m,P):
                    P_loc = {loc[i],loc[j],loc[k],loc[m],loc[n]}

        
        