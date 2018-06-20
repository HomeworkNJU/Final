# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:02:50 2018

@author: Alice_shu
"""

nums = input("请输入两个数：").split()
a = int(nums[0])
b = int(nums[1])
c = a * b
a_l = len(nums[0])
b_l = len(nums[1])
c_l = len(str(c))
Len = 0 
if a_l > b_l:
    nums[1] = " "*(a_l - b_l) + nums[1]  
    Len = a_l
else:
    nums[0] = " "*(b_l - a_l) + nums[0] 
    Len = b_l
if c_l > Len:
    nums[0] = " "*(c_l - Len) + nums[0]
    nums[1] = " "*(c_l - Len) + nums[1]
    Len = c_l

print("%s\n%s\n%s\n%d" % (nums[0],nums[1],"-"*(Len),a * b))
