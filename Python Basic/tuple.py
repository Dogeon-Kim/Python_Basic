# 튜플 자료형(순서, 중복, 수정(x), 삭제)

# 선언
a=()
b=(1,)
c=(11, 12, 13, 14)
d=(100, 1000, 'A', 'B', 'C')
e=(100, 1000, ('A', 'B', 'C'))

# 인덱싱
print('>>>>>>>>>>>>>>>>>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[-1])
print('d - ', list(d[-1]))
print('e - ', e[-1][0])
print('e - ', list(e[-1]), type(e[-1]))

# 수정X
# d[0] = 1111

# 슬라이싱
print('>>>>>>>>>>>>>>>>>>>>>>>>>')
print('d - ', d[0:3])

# 팩킹, 언팩킹
t=('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

(x1, x2, x3, x4)=t
print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))
