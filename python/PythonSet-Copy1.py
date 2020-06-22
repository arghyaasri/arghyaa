#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = int(input())
y = int(input())
z = int(input())
a = []
a.append(x)
a.append(y)
a.append(z)
max = 0
for i in a:
    if i % 2 != 0 and i > max:
        max = i
if max != 0:
    print("Largest odd number is ", max)
else:
    print("No odd number was entered")


# In[2]:


def right_justify(s):
    print(((70 - len(s)) * " ") , s)
right_justify("Cigna")


# In[3]:


a = []
for i in range(10):
    x = int(input())
    a.append(x)
max = 0
for i in a:
    if i % 2 != 0 and i > max:
        max = i
if max != 0:
    print("Largest odd number is ", max)
else:
    print("No odd number was entered")

