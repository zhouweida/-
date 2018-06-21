
# coding: utf-8

# 元组-tuple
#     元组可以看成是不可更改的lise

# In[7]:


#创建一个空元组
t = ()
print(type(t))

#创建只有一个值的元组
t = (1,)
print(t)
print(type(t))

#创建多个值的元组
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))

#使用其他结构创建元组
l = [1, 2, 3, 4, 5, 6]
t = tuple(l)
print(t)
print(type(t))


# ##元组的特性 
# -是序列表，有序
# -元组数据值可以访问，但是不能修改
# -元组的数据可以使任意类型的
# -总之，list所有的特性，除了修改，元组都具有

# In[8]:


#索引操作
t = (1, 2, 3, 4, 5)
print(t[2])


# In[1]:


#切片操作
t = (1, 2, 3, 4, 5, 6)
#下标从2开始，一直到最后，步长为2，进行切片
t1 = t[2::2]
print(t)
print(t1)
print(id(t))
print(id(t1))


# In[5]:


#成员检测
t = (1, 2, 3)
if 2  in t:
    print('yes')
else:
    print('no')
    


# In[8]:


# 元组的遍历
# 1、单层元组的遍历
t = (1, 2, 3, 'maomao', 'hehe')
for i in t:
    print(i, end=" ")
    


# In[9]:


# 2、双层元组的遍历
t = ((1, 2, 3),(5, 6, 7), 'maomao')
for i in t:
    print(i)


# In[10]:


# 2个数值的交换
a = 1
b = 3
print(a)
print(b)

print('-' * 30)

a, b = b, a
print(a)
print(b)

