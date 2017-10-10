
# coding: utf-8

# In[1]:

print(1+2)
print(5+6+7+8+9+10)


# In[2]:

print(8-100+20*5)
print(3.142*8)
print((973*863+985*211)/2011)


# In[4]:

n=2
n=5
m=7.2
print(1+2+3+4+n)
print(1+2+3+4-m)


# In[7]:

n=0
n=n+1
print(n)
n=n+2
print(n)
n=n+3
print(n)


# **compare**

# In[9]:

print(10>5)             #正确执行，打印True
print(10<1.1)           #正确执行，打印False
flag=False              #flag为逻辑类型的变量，值为False
print(flag)             #正确执行


# **while**

# In[6]:

# 4个空格是python语言的代码缩进，用来来划分程序层次
# i=i+1与print(i)是连续两行，且缩进相同，因此属于同一层次，属于同一层次的一或多行代码称为代码块。处在循环内部层次的代码块被称为循环体。
n=7
i=0
while i<n:
    i=i+1       #注意，i前面须敲4次空格
    print(i)    #注意，print前面须敲4次空格


# In[10]:

n=100
i=0
total=0
while i<n:          #注意条件表达式中的i随循环每次在变化
    i=i+1
    total=total+i
print(total)


# **input()**

# In[13]:

# input()函数从键盘接受输入，以回车作为输入结束，键盘输入的所有字符均被视为字符串，该字符串作为input()函数的值
n=input()
print(n)

# n=input()
# print(n+100)
# 结果提示TypeError,程序认为我们在提示框中输入的100是字符串，而字符串与数字相加没有定义，我们需要在程序中，将字符串转换为整型数


# In[14]:

n=input()
n=int(n)    #将n从字符串转换成整型
print(n+100)


# In[27]:

# 直接使用input()函数获得用户输入的时候，用户往往不知道需要做什么，其实可以在括号内键入任意字符串，用以提示用户
n = input('请输入一个整数，按回车结束。')
print(n)


# **转换为整型**

# In[16]:

# int()函数可将其括号内部的对象转换为整型。注意并非所有对象均可直接转为整型。
int('4078')     #可以
int(4078)       #可以
int(407.8)      #可以


# **常用数学运算符**

# In[17]:

print(4+6)      #运算符:'+'。功能：加法。结果：10
print(3.5-2)    #运算符:'-'，功能：减法。结果：1.5
print(9*9)      #运算符:'*'，功能：乘法。结果：81
print(5/2)      #运算符:'/'，功能：除法。结果：2.5
print(5**3)     #运算符:'**'，功能：乘幂。结果：125
print(5//2)     #运算符:'//'，功能：整除(舍去小数部分)。结果：2
print(7%3)      #运算符:'%'，功能：求余数(模)。结果：1


# In[19]:

# n=10
#   n=10      #对齐错误`IndentationError`


# **自更新运算**

# In[20]:

i = 0
i = i + 1       #自加运算
print(i)
i = 0
i += 1          #自加运算与赋值合并
print(i)
i = 0
i = i - 1       #自减运算
print(i)
i = 0
i -= 1          #自减运算与赋值合并
print(i)
i = 10
i = i * 10      #自乘运算
print(i)
i = 10
i *= 10         #自乘运算与赋值合并
print(i)
i = 10
i = i / 10      #自除运算
print(i)
i = 10
i /= 10         #自除运算与赋值合并
print(i)
i = 10
i = i % 3       #自求余运算
print(i)
i = 10
i %= 3         #自求余运算与赋值合并
print(i)
i = 10
i = i // 3     #自整除运算
print(i)
i = 10
i //= 3        #自整除运算与赋值合并
print(i)
i = 10
i = i ** 3     #自乘幂运算
print(i)
i = 10
i **= 3        #自乘幂运算与赋值合并
print(i)


# In[22]:

'''
这是一段注释
作为多行注释的示例
也是含有空行程序的示例
'''
# python语言的注释除了以#为开头的单行注释以外，还存在多行注释。


# **比较运算符**

# In[23]:

print(10 == 10)       #运算符：'=='。说明：等于。表达式值：True
print(10 != 10)       #运算符：'!='。说明：不等于。表达式值：False
print(10 > 5.1)       #运算符：'>'。说明：大于。表达式值：True
print(10.2 < 5)       #运算符：'<'。说明：小于。表达式值：False
print(5 >= 10)        #运算符：'>='。说明：大于等于。表达式值：False
print(5 <= 10)        #运算符：'<='。说明：小于等于。表达式值：True


# In[25]:

# 比较运算符甚至可以进行字符串之间的比较，会得到基于字母顺序的比较结果。但是python不允许用除了==及!=外的比较运算符对不同类型的对象进行比较
print('apple' > 'banana')
print('red' == 'red')
print('red' == 10)          #可以，不同类型，所以False
print('red' != 10)  
# print('red' >= 10)          #错误，不同类型


# **逻辑运算符**

# In[26]:

a = True
b = False

print(a and b)
print(a and True)
print(False and b)
print(a or b)
print(b or True)
print(not a)
print(not b)
print(not a and b)


# # 实践与练习
# **练习1:由用户从键盘给定任意正整数n，打印n!**

# In[30]:

n = int(input('请输入一个正整数，以回车结束。'))

i = 1
total = 0

while i <= n:
    i = i + 1
    total = total * i
    
print(total)


# **实践1：键入如下代码并观察执行结果。**

# In[31]:

name = input('请输入你的姓名，以回车结束。')
print('你好', name)

n = int(input('请输入一个正整数，以回车结束。'))
m = int(input('请输入一个正整数，以回车结束。'))

print('两个数的和是：', m+n)
print('再见！', name)


# **练习2：仿照实践1，写出由用户指定整数个数，并由用户输入多个整数，并求和的代码。**

# In[ ]:




# **练习3：用户可以输入的任意多个数字，直到用户不想输入为止。**

# **练习4：用户可以输入的任意多个数字，直到输入所有数字的和比当前输入数字小，且输入所有数字的积比当前输入数字的平方大。**

# In[ ]:



