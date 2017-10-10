
# coding: utf-8

# # 练习1:由用户从键盘给定任意正整数n，打印n!

# In[4]:


n = int(input('请输入一个正整数，以回车结束。'))

i = 0
total = 1

while i < n:
    i = i + 1
    total = total * i
    
print(total)


# # 实践1：键入如下代码并观察执行结果。

# In[5]:


name = input('请输入你的姓名，以回车结束。')
print('你好', name)

n = int(input('请输入一个正整数，以回车结束。'))
m = int(input('请输入一个正整数，以回车结束。'))

print('两个数的和是：', m+n)
print('再见！', name)


# # 练习2：仿照实践1，写出由用户指定整数个数，并由用户输入多个整数，并求和的代码。

# In[6]:


user = input('请输入您的姓名，以回车结束。')
print('你好', user)

n = int(input('请指定整数个数，以回车结束。'))
i = 0
total = 0

while i < n:
    m = int(input('请输入一个正整数，以回车结束。'))
    total = total + m
    i = i + 1

print('这些整数的和是：', total)
print('再见！', user)


# # 练习3：用户可以输入的任意多个数字，直到用户不想输入为止。

# In[8]:


user = input('请输入您的姓名，以回车结束。')
print('你好', user)
i = 0
while i == 0:
    m = input('请输入一个数字，结束请输入q:')
    if m == 'q': break
    print(m)

print('再见！', user)


# # 练习4：用户可以输入的任意多个数字，直到输入所有数字的和比当前输入数字小，且输入所有数字的积比当前输入数字的平方大。

# In[ ]:


user = input('请输入您的姓名，以回车结束。')
print('你好', user)

i = 0
total = 0
mul = 1

while i==0:
    m = int(input('请输入一个数字，结束请输入q:'))
    total = total + m
    mul = mul * m
    mi = m ** 2
    if ((total < m )and (mul > mi)) : break
    print('此时数字，总和，乘积,该数字的平方分别是：',m,total,mul,mi)

print('该数字是：',m)
print('再见！', user)

