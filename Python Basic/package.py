# 패키지 작성
# 파이썬은 패키지로 기능적으로 구분해서 관리한다.
# 상대경로: ..(부모 경로), .(현재디렉토리)->모듈 내부에서만 사용

# 예1
from cmath import sin
from operator import mod
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예2
from sub.sub1 import module1 as m1
from sub.sub2 import module2 as m2

m1.mod1_test1()
m1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

# 예3
from sub.sub1 import *

module1.mod1_test1()
