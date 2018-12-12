#!/usr/bin/env python
# coding: utf-8

# In[1]:


file=open("task1.bin")
Array=file.readlines()
data_size=Array[0]
data_size=int(Array[0],32)
if data_size>0x7FFFFFFF:
    data_size-=0x100000000
print(data_size)


# In[2]:


image_size=int(Array[1],32)
if image_size>0x7FFFFFFF:
    image_size-=0x10000000
    print(image_size)


# In[3]:


import numpy as np
Dt_array=np.empty([data_size-1])


# In[4]:


for i in range(len(Array)):
    if(i!=0):
        image_size=int(Array[i],32)
        if image_size>0x7FFFFFFF:
            image_size-=0x10000000
    Dt_array[i-1]=image_size


# In[5]:


Data_arr= Dt_array.astype(np.int32)


# In[6]:


ip=0
sp=data_size


# In[7]:


def f(v):
    sp = sp - 1
    Data_arr[sp] = v

def g():
    v = Data_arr[sp]
    sp = sp + 1
    return v


# In[8]:


def Decode(Instruction):
    Ibits = bin(Instruction)[2:].zfill(32)
    binop = Ibits[31]
    operation = Ibits[-8:-1]
    optional_data = Ibits[0:24]
    return binop, operation, optional_data


# In[9]:


while True:
    instruction = Data_arr[ip]
    ip = ip + 1
    binop, operation, optional_data = Decode(instruction)
    if(int(binop,2) == 0):
        if(int(operation,2) == 0):
            sp = sp + 1
            
        if(int(operation,2) == 1):
            f(optional_data)
            
        if(int(operation,2) == 2):
            f(ip)
            
        if(int(operation,2) == 3):
            f(sp)
            
        if(int(operation,2) == 4):
            addr = g()
            f(Data_array[addr])
            
        if(int(operation,2) == 5):
            st_data = g()
            addr = g()
            Data_array[addr] = st_data
            
        if(int(operation,2) == 6):
            cond = g()
            addr = g()
            if (cond != 0):
                ip = addr
                
        if(int(operation,2) == 7):
            if (g() == 0):
                f(1)
            else:
                f(0)
            
    elif(int(binop,2) == 1):
        a = g()
        b = g()
        if(int(operation,2) == 0):
            f(a+b)
            
        elif(int(operation,2) == 1):
            f(a-b)
            
        elif(int(operation,2) == 2):
            f(a*b)
            
        elif(int(operation,2) == 3):
            f(int(a/b))
            
        elif(int(operation,2) == 4):
            f(int(a&b))
        
        elif(int(operation,2) == 5):
            f(int(a|b))
            
        elif(int(operation,2) == 6):
            f(a**b)
            
        elif(int(operation,2) == 7):
            f(int(a==b))
            
        elif(int(operation,2) == 8):
            f(int(a<b))
            


# In[ ]:




