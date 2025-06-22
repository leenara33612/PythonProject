"""
파일명: HomeWork

반복문 안에 반복문

   *
  ***
 *****
*******
 *****
  ***
   *

Hint: 위이래 절반으로 나눠서 시작
      좌우 절반으로 나눠서 시작
      j를 i가 들어가는 함수로 정의하기
      while, if, elif, else 사용
"""

i = 0
while i <7:
    j = 0
    while j < 7:
        if i < 4:
            if j < 3 - i:
                print(' ', end='')
            elif j > 3 + i:
                print(' ', end='')
            else:
                print('*', end='')

        else:
            if j < i - 3:
                print(' ', end='')
            elif j > 9 - i:
                print(' ', end='')
            else:
                print('*', end='')
        j += 1
    print()
    i += 1
