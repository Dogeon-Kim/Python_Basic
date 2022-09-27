# 외장(External) 함수 : 개인, 재단, 기업체
# 실제 개발에서 많이 쓰임
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예1
from cmath import pi
import sys
print(sys.argv)

# 예2(강제 종료)
# sys.exit

# 예3
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle

# 예4(쓰기)
f= open("test.obj", 'wb')
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj,f)
f.close()

# 예5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# os : 환경변수, 디렉토리(파일) 처리관련, 운영체제 작업관련
# mkdir, rmdir(비어 있으면 삭제), rename...

# 예6
import os
print(os.environ)
print()
print(os.environ["USERNAME"])

#예7
print(os.getcwd())

# time : 시간 관련 찰
import time

# 예8
print(time.time())
# 예9
print(time.localtime(time.time()))
# 예10(간단 표현)
print(time.ctime())
# 예11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 예12(시간 간격 발생)
for i in range(5):
    print(i)
    # time.sleep(1)

#random : 난수
import random

# 예13
print(random.random()) #0~1 사이의 실수
# 예14
print(random.randint(1, 45)) #1~45
print(random.randrange(1, 45)) #1~44

# 예15(섞기)
d = [1,2,3,4,5]
random.shuffle(d) #표본 추출 시
print(d)
# 예16(무작위 선택)
c = random.choice(d)
print(c)

# Webbrowser : 본인 OS의 웹브라우저 실행
import webbrowser

webbrowser.open("https://google.com")
webbrowser.open_new("https://google.com") #new window(Crawling할 때)
