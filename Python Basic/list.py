# 리스트(순서, 중복, 수정, 삭제) : 자유로운 우체함

# 선언
a=[]
b=list()
c=[10, 20, 30, 40]
print(len(c))
d=[1000, 10000, 'A', 'B']
e=[1000, 10000, 'A', 'B', [101, '102', 103]]

# 인덱싱
print('---------------------------')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[1]+d[0])
print('d - ', d[-1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('---------------------------')
print('d - ', d[0:2])
print('e - ', e[-1][1:3])

# 리스트 연산
print('---------------------------')
print('c + d', c+d)
print('c * 3', c * 3)
print('Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)
print('---------------------------')
temp = c
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('---------------------------')
c[0] = 4
print('c - ', c)
c[1:2] = [['a', 'b', 'c']] #중첩(list 안에 list)
print('c - ', c)
c[1:3]=[]
print('c - ', c)
del c[2]
print('c - ', c)

# 리스트 함수
a=[5, 2, 3, 1, 4]
print('a - ', a)
a.append(10)
print('a - ', a)
a.append(20)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(2), a[2])
a.insert(2, 7777)
print('a - ', a)
a.remove(10)
print('a - ', a)
a.pop()
print('a - ', a)
print('a - ', a.pop()) #마지막 값 출력
print('a - ', a)
print('a - ', a.count(20)) #해당 숫자 개수 출력(없으면 0)
ex=[88, 99]
a.extend(ex)
print('a - ', a)

# 반복문 활용
while a:
    data = a.pop()
    print(data)
    



