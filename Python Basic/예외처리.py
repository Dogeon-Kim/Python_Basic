# 예외 종류
# --> SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError.....
# 문법적으로 예외가 없지만, 코드 실행단계에서 발생하는 예외도 중요!!
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남김
# 3. 예외는 던져짐
# 4. 예외 무시

# Syntax Error : 문법적 오류
# print('error)

# ZeroDivisionError
# print(100/0) 

# IndexError
# x=[10, 20, 30]
# print(x[5])

# KeyError
# dic={'name':'Kim'}
# print(dic['hobby'])

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError
# x=[10, 20, 30]
# x.romove(50)

# TypeError
# x=[1, 2]
# y=(1, 2)
# z='test'
# print(x+list(y))

# 예외처리 방법
# try : 에러가 발생 할 가능성 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행


from typing import final


name=['Kim', 'Lee', 'Park']

# 예1
# try:
#     z='Kim'
#     x=name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except ValueError:
#     print("not fount it! - Occcurred ValueError")
# else:
#     print("OK! else.")

# print()
# print('continue')

# 예2
# try:
#     z='Kim'
#     x=name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception:
#     print("not fount it! - Occcurred ValueError")
# else:
#     print("OK! else.")

# print()
# print('continue')

# # 예3 
# try:
#     z='Kim'
#     x=name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception as e: 
#     print(e)
#     print("not fount it! - Occcurred ValueError")
# else:
# #     print("OK! else.")
# finally:
#     print('OK! finally')
# print()
# print('continue')