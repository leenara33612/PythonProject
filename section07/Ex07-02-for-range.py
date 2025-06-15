"""
파일명: Ex07-02-for-range.py

for 문과 range()

range() 함수 # range() 좀 더 자세하게 확인하기
    연속된 숫자를 만들어주는 함수

    ex)range(10) => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
       range(1, 10) => 1, 2, 3, 4, 5, 6, 7, 8, 9
"""
dan = 2

# range(stop)

for n in range(10):
    print(f'{dan} x {n} = {dan * n}')

print()

# range(start, stop)
dan = 3
for n in range(1, 10):
    print(f'{dan} x {n} = {dan * n}')

print()

# range(start, stop, step)
dan = 4
for n in range(1, 10, 2): # 1부터 2씩 증가 < 10
    print(f'{dan} x {n} = {dan * n}')
