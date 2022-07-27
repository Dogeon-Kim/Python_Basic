# 집합(Sets) 순서/중복(X)

# 선언
from locale import YESEXPR


a = set()
b = set([1, 2, 3, 4])
c = set([1, 2, 3, 4, 'A', 'B'])
d = {'AA', 'BB', 'CC'}

print('a - ', type(a))

t=tuple(b)
print('t - ', type(t), t)

s1 = ([1, 2, 3, 4, 5, 6])
s2 = ([4, 5, 6, 7, 8, 9])

# 교
print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))

# 합
print('s1 | s2', s1 | s2)
print('s1 | s2', s1.union(s2))

# 차
print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))