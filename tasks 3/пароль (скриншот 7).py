# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:49:55 2023

@author: Pupil
"""

p='Parol_9:9'
b=[]
m='сложность пароля - '
f=1
for i in range(len(p)):
    if p[i].isdigit()==True:
        b.append(f)
        break
for i in range(len(p)):
    if p[i]=='_' or p[i]=='!' or p[i]=='=' or p[i]=='+':
        b.append(f)
        break
if len(p)>7:
    b.append(f)
for i in range(len(p)):
    if p[i].isalpha()==True:
        if p[i]==p[i].upper():
          b.append(f)
          break
for i in range(len(p)):
    if p[i]==':':
        b.append(f)
        break
s=sum(b)
o=m+str(s)
print(o)
    
