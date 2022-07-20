'''
int: 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
'''

float = 10.0
str1 = 'A'
str2 = 'B'
list = [str, str2]
dict = {
    "name" : "Machine Learning",
    "version":2.0
} #브래이스

tuple = (7, 8, 9)
set = {7, 8, 9}

print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 연산자
# 몫: //
# abs(x) : 절대값
# pow(x, y) : x의 y제곱 == x**y
big_int = 123409876543212367835678
print(big_int)

a = 3. #3.0으로 인식
#print(float(a))
print(int(a))
print(str(a))
print(complex(a))
print(complex('3'))

print(abs(-2000))
# 추가 내용
x, y = divmod(100, 8)
print(x, y)
print(pow(2, 3))

# 외부 모듈
import math
print(math.pi)
print(math.ceil(5.1))# 천장!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(math.floor(5.9))