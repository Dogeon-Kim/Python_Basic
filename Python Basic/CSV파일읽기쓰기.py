# CSV
from asyncore import read
import csv
# 예1
with open('Python Basic\\resource\\test1.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    #next(reader) #Header Skip
    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader)) #__iter__
    print()

    for c in reader:
        #print(c)
        print(''.join(c))

# 예2
with open('Python Basic\\resource\\test1.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter=',')

    for c in reader:
        print(c)

# 예3
with open('Python Basic\\resource\\test1.csv', 'r', encoding='UTF-8') as f:
    reader = csv.DictReader(f)

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    # for c in reader:
    #     print(c)

    for c in reader:
        for k, v in c.items():
            print(k,v)
        print('-'*10)

# 예