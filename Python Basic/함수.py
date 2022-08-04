# 예1
from multiprocessing.sharedctypes import Value


def first_func(w):
    print("Hello, ", w)

word="Goodbey"

first_func(word)

# 예2
def return_func(w1):
    value='Hello, ' + str(w1)
    return value

x=return_func("GoodBye")
print(x)

# 다중반환
def func_mul(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return y1,y2,y3
x,y,z=func_mul(10) #언패킹
print(x, y, z)

# tuple return
def func_mul2(x):
    y1=x*10
    y2=x*20
    y3=x*30
    return (y1,y2,y3)

q=func_mul2(10) #패킹
print(q)
print(func_mul2(10))

# 중요
# *args, **kwargs

# *args(언패킹)
def args_func(*args): #매개변수명은 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('---------------------------------')
args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs(언패킹) //dictionary
def kwargs_func(**kwargs):
    for v  in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-------------------------------')
kwargs_func(name1='Lee', name2='Kim')








