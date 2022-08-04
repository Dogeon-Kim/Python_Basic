# 기본형식
print(type(True)) #0이 아닌수, "abc", [1,2,3,4], (1,2,3,4)...
print(type(False)) #0, "", [], (), {}

# 예1
if 'aaa':
    print('Good')

# 예2
if False:
    print('Bad!')
else:
    print('Good!')

# 관계연산자 : >, >=, <, <=, ==, !=
a=1
b=2
print(a!=b)

city=""
if city:
    print("You are in:", city)
else:
    print("Pleae enter your city")

# 논리연산자(중요): and, or, not
a=75
b=40
c=10

print('and', a>b and b>c) #a>b>c
print('or', a>b or b>c)
print('not', not(a>b and b>c))

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('call1:', 3+100 > 7+10)
print('call2:', 5+10 > 3 and 7+3 == 10)

# 다중조건문
num=90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('Grade : F')

# 중첩조건문
grade='A'
total=95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 90%')
    else:
        print('장학금 50%')
else:
    print('mc')

# in, not in 
a=[10, 20, 30]
b={10, 20, 30}
c=dict(name="Kim", country="Korea", age=17)
d=(10, 12, 14)

print(15 in a)
print(90 in b)
print(12 not in d)
print("name" in c)
print("Korea" in c.values())
