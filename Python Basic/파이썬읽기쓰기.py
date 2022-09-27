# 읽기 모드 r, 쓰기모드 w, 추가모드 a(append), 텍스트모드 t, 바이터리모드 b
# 상대경로('../, ./'), 절대경로('C:\.....')

# 파일 읽기(Read)
# 예1
# f = open('C:\\Users\\kdk54\\OneDrive\\바탕 화면\\Python_Basic\\Python Basic\\resource\\it_news.txt')
import ctypes


f = open('Python Basic\\resource\\it_news.txt', 'rt', encoding='UTF-8')

# 속성 확인
print(dir(f))
# encoding 확인
print(f.encoding)
# mode 확인
print(f.mode)
# 컨텐츠
cts = f.read
print(cts)
# close
f.close 

# 예2(많이 사용하는 방법)
with open('Python Basic\\resource\\it_news.txt', 'rt', encoding='UTF-8') as f: #close 필요X
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
print()

# 예3
# read() : 전체 읽기, read(10): 10 Byte 일기
with open('Python Basic\\resource\\it_news.txt', 'rt', encoding='UTF-8') as f: #close 필요X
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0, 0) #처음으로 #seek(from, to)
    c = f.read(20)
    print(c)

# 예4
# readline : 한 줄 씩 읽기
with open('Python Basic\\resource\\it_news.txt', 'rt', encoding='UTF-8') as f: #close 필요X
    line = f.readlines()
    print(line)
    line = f.readlines()
    print(line)


with open('Python Basic\\resource\\it_news.txt', 'rt', encoding='UTF-8') as f:
    while True:
        line = f.readlines()
        if not line: break
        print(line)


# 예5 (많이 사용)
# readlines : 전체를 읽은 후 라인 단위로 리스트 저장
with open('Python Basic\\resource\\it_news.txt', 'rt', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    for c in cts:
        print(c, end='\n')

# 파일 쓰기(write)

# 예1
with open('Python Basic\\contents1.txt', 'w', encoding='UTF-8') as f:
    f.write('I love BSSM\n')
# 예2
with open('Python Basic\\contents1.txt', 'at', encoding='UTF-8') as f:
    f.write('I love BSSM\n')
# 예3(많이씀)
# writelines : 리스트 --> 파일
with open('Python Basic\\contents1.txt', 'w', encoding='UTF-8') as f:
    list = ['orange\n', 'apple\m', 'banana\n', 'melon\n']
    f.writelines(list)
# 예4
with open('Python Basic\\contents1.txt', 'w', encoding='UTF-8') as f:
    print('Test Text Write!!', file=f)
    print('Test Text Write!!', file=f)
    print('Test Text Write!!', file=f)