
# coding: utf-8

# In[12]:


#定义一个函数，打印出九九乘法表
def _(row):
    for col in range (1,row+1):
        print (row * col,end=" " )
    print("")
for row in range(1,10):
    _(row)
    


# In[5]:


#斐波那契数列（返回值不用等号赋值）
#1， 1， 2， 3， 5， 8， 13， 。。。 
#n = （n-1） + (n-2)
def fib(n):
    #第一个值是1
    if n == 1:
        return 1
    #第二个值是1
    if n == 2:
        return 1
    #之后都是前2个值之和
    return fib(n-1) + fib(n-2)
print(fib(10))


# 汉诺塔问题
#     规则：
#     1、每次移动一个盘子
#     2、任何时候都是大盘子在下，小盘子在上。
#     方法：
#     1、n = 1：直接把A上的一个盘子移动到C上面， A->C
#     2、n = 2：
#             A.把小盘子从A移动到B上面， A->B
#             B.把大盘子从A移动到C上面， A->C
#             C.把小盘子从B移动到C上面， B->C
#     3、n = 3：
#             A.把A上的2个盘子，借助C塔，移动到B上面，调用递归
#             B.把A上的大盘子，移动到C上面， A->C
#             C.把B上的2个盘子，借助A塔，移动到C上面，调用递归
#     4、n = n:
#             A.把A上的（n-1）个盘子，借助C塔，移动到B上面，调用递归
#             B.把A上的大盘子，移动到C上面， A->C
#             C.把B上的（n-1）个盘子，借助A塔，移动到C上面，调用递归

# In[4]:


#汉诺塔
def hanno(n, a, b, c):
    '''
    n表示盘子数量
    a表示第一个塔
    b表示第二个塔
    c表示第三个塔
    '''
    if n == 1:
        print(a, '-->', c)
        return None
    
    if n == 2:
        print(a, '-->', b)
        print(a, '-->', c)
        print(b, '-->', c)
        return None
    
    #把a塔上的n-1个盘子，借助c塔，移动到b塔上面，递归
    hanno(n-1, a, c, b)
    #把a塔上的大盘子移动到c塔
    print(a, '-->', c)
    #把b塔上的n-1个盘子，借助a塔，移动到c塔上面，递归
    hanno(n-1, b, a, c)
        
a = 'A'
b = 'B'
c = 'C'
n = 1
hanno(n, a, b, c)


# In[5]:


n = 2
hanno(n, a, b, c)


# In[7]:


n = 3
hanno(n, a, b, c)


# In[1]:


# append插入一个内容，在末尾追加
a = [1, 3, 4, 5, 7, 8]
print(a)
a.append(10)
print(a)


# In[4]:


# insert:制定位置插入一个内容
# insert（index，data）（索引，内容），插入位置是index的前面
print(a)
a.insert(4, 100)
print(a)


# In[6]:


# del删除
# pop 从队尾拿出一个元素，既把最后一个元素取出
print(a)
last = a.pop()
print(last)
print(a)


# In[ ]:


# remove:在列表中删除指定位置的值
# 如果使用remove删除的值不存在，程序则会报错
# 即删除list指定值的操作，应该用try。。。。excepty语句，或者先进行判断

#if x in list:
#    list.remove(x)


# In[9]:


# clear:清空列表所有元素
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))

# 如果不需要保持列表地址不变，则清空列表可以用一下方式
# a = list（）
# a = []


# In[12]:


# reverse:翻转列表内容，保持地址不变

a = [1, 2, 3, 5, 8, 10]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))


# In[13]:


# extend:扩展列表，把一个列表直接拼接到另一个列表上(地址不变)

a = [1, 2, 3, 5, 8, 10]
b = [20, 99, 100]
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))


# In[14]:


# count：查找列表中指定值或者元素的个数

a = [1, 2, 3, 5, 8, 10]
a.append(3)
a.insert(0,3)
x = a.count(3)
print(x)
print(a)


# In[21]:


# copy：复制一个列表(浅拷贝)

#列表类型变量赋值示例
a = [1, 2, 3, 4, 5, 666]
print(a)
#list类型，简单的赋值操作，就是传地址，既a与b指向同一个地址
b = a
b[3] = 77
print(a)
print(b)

print('*' * 30)

#为了解决上述问题，list赋值可以采用copy函数
b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))

print('*' * 30)

b[3] = 100
print(a)
print(b)


# In[23]:


# 浅拷贝和深拷贝的区别

#copy函数是浅拷贝函数，只拷贝一层内容
a = [1, 2, 3, [1, 2, 3]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
b[3][2] = 333
print(a)
print(b)

#深拷贝需要使用特定工具（模块）

