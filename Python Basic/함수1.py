# abs
# all: iterable 요소 검사
print(all([0,2,3])) #and
# any: iterable 요소 검사
print(any([0,0,1])) #or

# char, ord (chr:아스키->문자, ord:문자->아스키)
print(chr(67))
print(ord('C'))

# enumerate (인덱스 번호 및 값 같이 데이터 처리)
for i, name in enumerate(['a', 'b', 'c']):
    print(i, name)

# filter : 반복가능한 객체 요소 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2
print(list(filter(conv_pos, [-10, -5, 0, 3, 5])))

# 길이 
print(len('abcdefg'))

# 최대, 최소
print(max([1,2,4]))
print(min([1,2,4]))
print(min('wertyuiolmnbvcdrtyuiklmnbvcdftyu'))

# map : 반복 가능한 개체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)
print(list(map(conv_abs, [1,2,34,-1,56,6])))

