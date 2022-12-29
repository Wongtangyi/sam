# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:39:58 2022

@author: user
"""

for a in range(1,6):
    for x in range(a):
        print(x,end="")
    print()
    
"""
第一個作業
1
22
333
4444
55555

第二個作業
55555
4444
333
22
1

第三個作業
999999999
7777777
55555
333
1
"""
#第一個作業
for a in range(1,6): #控制列印數字
    sum = a
    for x in range(a): #控制列印次數
        print(sum,end="")
    print()
    
#第二個作業
for a in range(5,0,-1):
    sum = a
    for x in range(a):
        print(sum,end="")
    print()
    
#第三個作業   
for a in range(9,0,-2):
    sum = a
    for x in range(a):
        print(sum,end="")
    counter = a-2
    print()        
    