#print()
#print("Python Star!")
#print("Python Star!!")
#print('''Python Star!''')
#print("""Python Star!""")

# Sperator
#print('p', 'y', 't', 'h', 'o', 'n', sep='-')

# end option
#print("Welcome to", end=' ')
#print("IT Highschool", end=' ')
#print('classroom', end=' ')

# file option
#import sys
#print("Learn Python", file=sys.stdout) #저장 파일 경로

# format 사용(d, f, s)
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', '2'))
print('{1} {0}' .format('one', 'two'))
# %s
print('%10s' % ('nice1111')) #왼쪽에서 부터
print('%-10s' % ('nice1111')) #오른쪽에서 부터
print('%.5s' % ('nice')) #채우기
print('%-.5s' % ('nicestudy')) #자르기
# %d
print('%4d' % (42))
# %f
print('%f' % (3.141223325436456))
print('%.1f' % (3.141223325436456))
print('%06.1f' % (3.141223325436456)) #6자리 남는 칸은 0으로 채움