# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:29:45 2018

@author: lenovo
"""

def analyze(s):
    out=[]
    for i in range(0,len(s)):
        if(s[i]==')'):
            m=''
            for j in range(i-1,0,-1):
                if(s[j]=='('):
                    break
                else:
                    m+=s[j]
            m=m[::-1]
            out.extend(analyze(m))
    for i in range(0,len(s)):
        if(s[i]=='*' or s[i]=='/'):
            for j in range(i-1,0,-1):
                if(s[j].isdigit()):
                    out.append(int(s[j]))
                    break
            for j in range(i+1,len(s)):
                if(s[j].isdigit()):
                    out.append(int(s[j]))
                    break
    for i in range(0,len(s)):
        if(s[i]=='+' or s[i]=='-'):
            for j in range(i-1,-1,-1):
                if(s[j].isdigit()):
                    out.append(int(s[j]))
                    break
            for j in range(i+1,len(s)):
                if(s[j].isdigit()):
                    out.append(int(s[j]))
                    break
    return out
                
s=input("please input calculation:")
out=analyze(s)
print(out)
