"""
파일명: Ex17-03-Exception.py
"""

try:
    a = int(input('제수를 입력하세요 >>>'))
    b = int(input('피제수를 입력하세요 >>>'))
    print(f'{a} / {b}={a / b}')

except ZeroDivisionError as zde:
    print('0으로 나눌 수 없습니다')
    print(zde)
except ValueError as ve:
    print('정수만 입력할 수 있습니다')
    print(ve)
except:
    print('예외가 발생했습니다')

print('프로그램 종료')