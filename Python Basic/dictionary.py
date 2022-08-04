a={
    'name': 'Kim',
    'phone': '1234',
    'birth' : '06'
}
c = dict(
    Name = 'NiceMan',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
 )
print('c - ', type(c), c)

# 출력
print('c - ', c.get('Name1'))
print('c - ', c['City'])

# 추가
c['Address'] = '101-101'
c['Rank'] = [1, 2, 3, 4, 5]
print('c - ', c)
print('c - ', len(c))

# method
print('c - ', c.keys())
print('c - ', c.values())
print('c - ', c.pop('Name'))
print('c - ', 'Wow'  in c)

c['G']
