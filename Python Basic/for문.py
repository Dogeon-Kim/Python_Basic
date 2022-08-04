'''
# for in collection
#       <loop body>

from traceback import print_exc


for v1 in range(10):
    print('v1 is :', v1)

for v2 in range(1, 11):
    print('v2 is :', v2)

for v3 in range(1, 11, 2): #1,3,5,7,9
    print('v3 is :', v3)

for v4 in range(0, 101, 2):
    print('v4 is :', v4)

sum1=0
for v5 in range(1, 1001): 
    sum1+=v5
    print('1~1000 Sum :', sum1)
    print('1~1000 Sum :', sum(range(1,1001))) #sum(기본 List)
    print(type(range(1,11)))
    print('1~1000 4의 배수 Sum :', sum(4,1001,4))
'''
##########################################333
# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴함수: range, reversed, enumerate, filter, map, zip

# 예1
names=['Kim', 'Park', 'Choi', 'Won', 'Yoo', 'Cho']
for n in names:
    print('You are :', n)

# 예2
lotto_numbers=[11,19,21,28,36,37]

for n in lotto_numbers:
    print("Current number : ", n)
    
word='Beautiful'
for s in word:
    print('word : ', s)

# 예3
my_info=dict(
    name='Kim',
    age=17,
    city='Changwon'
)

for k in my_info.keys():
    print('keys : ', k)
    print('value : ', my_info[k])
    print('value : ', my_info.get(k))

for k in my_info.values():
    print('value : ', k)

# 예4
name='PineApple'
for n in name:
    if n.isupper():
        print(n, end='')
    else:
        print(n.upper(), end='')

# for - else문
numbers=[14,3,2,4,5,11,15,24,26,24,46]
for num in numbers:
    if num==14:
        print('Found : 34!')
    else:
        print('Not found : ', num)

# continue
lt=["1", 2, 4, True, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type : ", v, type(v))

    # for - else문
numbers=[14,3,2,4,5,11,15,24,26,24,46]
for num in numbers:
    if num==14:
        print('Found : 314')
        break
    #else:
    #   print('Not found : ', num)
else:
    print('Not found : 14')


# 구구단 출력
for x in range(2, 10):
    for y in range(1, 10):
        print(x, 'x', y, '=', x*y)

# 변환
a='Kim'

print(reversed(a))
print(list(reversed(a)))
print(tuple(reversed(a)))
print(set(reversed(a)))
a = list(reversed(a))
print(a)
print(''.join(map(str, a)))
