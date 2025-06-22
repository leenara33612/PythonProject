"""
파일명: Ex12-05-random.py

random 모듈
    난수 생성 모듈
"""

import random

# 두 인자 사이 난수
print(random.randint(1, 10)) # 1 ~ 10 사이

# randrange - range 범위 난수 생성
print(random.randrange(10)) # 0 ~ 9 사이
print(random.randrange(1, 10)) # 1 ~ 9 사이
print(random.randrange(1, 10, 2)) # 1 ~ 9 2씩 증가(홀수만)

# 0이상 1미만 난수 생성
print(random.random())

if random.random() < 0.5:
    print('안녕하세요!!')
else:
    print('안녕하세요??')

# choice 함수 - 리스트에서 랜덤
seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))

# shuffle 함수 -임의로 섞는 함수
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)