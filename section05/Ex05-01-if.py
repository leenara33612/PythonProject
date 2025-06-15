"""
파일명: Ex05-01-if.py

조건문
    특정 조건에 따라 다른 코드를 실행하도록 하는 제어문
    * 들여쓰기를 사용하여 코드의 범위 정의
"""

a = 100
b = 200

# 1. if 문(조건식이 True로 나와야 실행된다)
if b > a:
    print('b는 a보다 크다.')

# 2. if ~ else 문
a = 7
b = 4

if b >= a: # False가 되면서 실행이 안됨
    print('b는 a보다 크거나 같다.')
else:
    print('b는 a보다 작다.')

# 3. if ~ elif ~ else(조건이 여러개 일때 사용하는 조건문)
age = 15

if age >= 19: # False라서 실행 안됨
    print('성인 입니다.')
elif age >= 13: # True라서 출력(뒤의 조건문이 실행되지 않음)
    print('청소년 입니다.')
elif age >= 8:
    print('어린이 입니다.')
else:
    print('영유아 입니다.')

print('프로그램 종료')# if 조건문안에 들어있지 않기 때문에 독립적으로 실행됨