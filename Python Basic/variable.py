n = 700

print(n*700)

print(n)
print(type(n))

# 동시선언
x = y = z = 700
print(x, y, z)

# 선언 
var = 75
var = 'Hello World'
print(var)
print(type(var))

# Object Reference
# 변수의 값 할당 상태
# 1.type에 맞게 Object 생성
# 2. 값을 생성 //값이 같으면 같은 id 사용
# 3. 출력
# ex 1)
print(300)
print(int(300))

# id(identity)확인 : Object의 고유값
m=800
n=655

print(id(m))
print(id(n))
print(id(m)==id(n))
print()

m=800
n=800
z=800

print(id(m))
print(id(n))
print(id(m)>id(n))
print()

# 고급개발로 보이는 방법
# Camel: numberOfCollege
# Pascal: NumberOfCollege
# Snake: number_of_college

