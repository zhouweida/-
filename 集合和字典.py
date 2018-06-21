
# coding: utf-8

# # 集合-set
# 一堆确定的无序的唯一的数据，集合中的每一个数据成为一个元素。

# In[9]:


# 集合的定义

s = set()
print(type(s))
print(s)


#如果只用大括号定义，则定义出来的是一个dict类型
#此时大括号一定要有值，否则定义出来的是一个dict

s = {2,3,4,5,6,7,8}
print(type(s))
print(s)


# # 集合的特征
# - 集合内数据无序，无法使用索引和分片
# - 集合内数据具有唯一性，可以用来排除重复数据
# - 集合内的数据，str，int，float，tuple，冰冻集合等等，即内部只能放置可哈希数据

# In[4]:


# 集合函数
# intersection:交集
# difference：差集
# union：并集
# issubset：检查一个集合是否是另一个集合的子集
# issuperset：检查一个集合是否是另一个集合的子集

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

s_1 = s1.intersection(s2)
print(s_1)

s_2 = s1.difference(s2)
print(s_2)

s_3 = s1.union(s2)
print(s_3)

s_4 = s1.issubset(s2)
print(s_4)


# In[6]:


#集合的数学操作
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

s_1 = s1 - s2
print(s_1)

#不支持加号操作


# frozen set:冰冻集合
# 冰冻集合就是不可以进行操作修改的集合

# In[7]:


#冰冻集合的创建
s = frozenset()
print(type(s))
print(s)


# # dict字典
# - 字典是一种没有顺序的组合数据，数据以键值对形式出现

# In[13]:


# 字典的创建

# 1、创建空字典1
d = {}
print(d)

# 2、创建空字典2
d = dict()
print(d)

# 3、创建有值的字典，每一组数据用冒号隔开，每一对键值用逗号隔开
d = {'one':1 , 'two':2 , 'three':3}
print(d)

# 4、用dict创建有值的字典1
d = dict({'one':1 , 'two':2 , 'three':3})
print(d)

# 5、用dict创建有值的字典2
# 利用关键字参数
d = dict(one=1 , two=2 , three=3)
print(d)


# # 字典的特征
# - 字典是序列类型，但是是无序的序列，所以不能进行分片操作，不能进行索引操作
# - 字典的数据每个都是由键值对组成，既k，v对
#     - key必须是可哈希的值，比如int，string，float，tuple，但是list，set，dict不行
#     - value：任何值

# # 字典常见操作

# In[19]:


# 访问数据

d = {"one":1 , "two":2 , "three":3}
# 注意访问格式
# 中括号内是键值，key
print(d["one"])

# 赋值操作
d["one"] = "yi"
print(d)

# 删除操作
# 使用del操作
del d["one"]
print(d)


# In[20]:


# 成员检测
# 成员检测是key的内容
d = {"one":1 , "two":2 , "three":3}
if 2 in d:
    print("value")
if "two" in d:
    print("key")
if ("two",2) in d:
    print("kv")


# In[28]:


# 遍历

# 使用for循环，直接用key值访问
d = {"one":1 , "two":2 , "three":3}
for k in d:
    print(k , d[k])
    
# 上面代码可以改写成如下
for k in d.keys():
    print(k , d[k])

# 只访问字典的值
for v in d.values():
    print(v)
    
# 以下特殊用法
for k , v in d.items():
    print(k , "--" , v)


# In[34]:


# 字典生成式
d = {"one":1 , "two":2 , "three":3}

# 常规的字典生成式
dd = {k:v for k,v in d.items()}
print(dd)

# 加限制条件的字典生成式
dd = {k:v for k,v in d.items() if v % 2 == 1}
print(dd)


# # 字典的相关函数

# In[1]:


# 通用函数：len max min dict
# str（字典）：返回字典的字符串格式
d = {"one":1 , "two":2 , "three":3}
print(str(d))


# In[2]:


# clear:清空字典
# items:返回字典的键值对组成的元组格式

d = {"one":1 , "two":2 , "three":3}
i = d.items()
print(type(i))
print(i)


# In[3]:


# keys:返回字典里的键组成的一个结构
k = d.keys()
print(type(k))
print(k)


# In[4]:


# values同理，一个可迭代的结构
v = d.values()
print(type(v))
print(v)


# In[5]:


# get:根据指定的键返回相对的值，好处是，可以设置默认值。
d = {"one":1 , "two":2 , "three":3}
print(d.get("one"))
# 不会报错，会返回一个none的默认值
print(d.get("onee"))
# get默认值是none，可以设置
print(d.get("onee" , 100))


# In[6]:


# fromkeys:使用指定的序列作为键，使用一个值作为字典的所有键的值
l = ["one" , "two" , "three"]
# 注意fromkeys的两个参数类型
# 注意fromkeys的调用主体（dict）
d = dict.fromkeys(l , "hahaha")
print(d)

