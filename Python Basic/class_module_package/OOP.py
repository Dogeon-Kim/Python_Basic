# OOP(Object Oriented Programming)
# 객체지향프로그래밍
# Self, 인스턴스 매소드, 인스턴스 변수

# 클래스 vs 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간(dictionary)
# 클래스 변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도 존재

# 예1
class Dog: #Object 상속
    # 클래스 속성
    species = 'firstdog' #클래스 변수

    #초기화 인스턴스 속성
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('mikky', 2)

# 비교
print(a==b, id(a), id(b), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog=2', b.__dict__)

# 인스턴스 속성
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species) #클래스 이름으로 접근
print(a.species) #인스턴스화 된 변수로 접근
print(b.species) #인스턴스화 된 변수로 접근





